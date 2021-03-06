# (pgbackup-E7nj_BsO) pgbackup $
# (pgbackup-E7nj_BsO) pgbackup $ vim src/pgbackup/cli.py

import argparse

known_drivers = ['local', 's3']

class DriverAction(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
            if driver.lower() not in known_drivers:
                parser.error("Unknown driver. Available drivers are 'local' & 'S3'")
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser = argparse.ArgumentParser(description="""
    Backup PostgreSQL databases to AWS S3 or locally.
    """)
    parser.add_argument('url', help='URL of database to backup')
    parser.add_argument('--driver',
            help='how & where to store the backup',
            nargs=2,
            metavar=("DRIVER", "DESTINATION")
            action=DriverAction,
            required=True)
    return parser


def main():
    import boto3
    from pgbackup import pgdump, storage
 
    args = create_parser().parser_args()
    dump = pgdump.dump(args.url)
    if args.driver == 's3':
        client = boto3.client('s3')
        storage.s3(client, dump.stdout, args.destination, 'example.sql')
    else:
        outfile = open(args.destination, 'w')
        storage.local(dump.stdout, outfile)
