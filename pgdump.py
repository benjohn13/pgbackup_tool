# pgdump module

# (pgbackup-E7nj_BsO) [pgbackup $]
# (pgbackup-E7nj_BsO) [pgbackup $] vim src/pgbackup/pgdump.py

import sys
import subprocess


def dump(url):
    try:
        return subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE)
    except OSError as err:
        print("Error: pg_dump not found")
        sys.exit(2)
