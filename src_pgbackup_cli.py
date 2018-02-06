# (pgbackup-E7nj_BsO) pgbackup $
# (pgbackup-E7nj_BsO) pgbackup $ vim src/pgbackup/cli.py

import argparse

class DriverAction(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
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
            action=DriverAction,
            required=True)
    return parser