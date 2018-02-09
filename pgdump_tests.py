# Tests for pgdump module

# (pgbackup-E7nj_BsO) [pgbackup $]
# (pgbackup-E7nj_BsO) [pgbackup $] vim tests/test_pgdump.py

import pytest
import subprocess
from pgbackup import pgdump

url = "postgres://bob:password@example.com:1234/db_one"


def test_dump_call_pg_dump(mocker):
    """
    Utilize pg_dump to interact with Database
    """
    proc = mocker.Mock()
    mocker.patch('subprocess.Popen', return_value=proc)
    assert pgdump.dump(url) == proc
    subprocess.Popen.assert_called_with(['pg_dump', url], stdout=subprocess.PIPE)


def test_dump_handles_oserror(mocker):
    """
    pgdump.dump returns a reasonable error if pg_dump is not installed
    """
    mocker.patch('subprocess.Popen', side_effect=OSError("no such file"))
    with pytest.raises(SystemExit):
        pgdump.dump(url)
