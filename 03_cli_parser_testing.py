# Test Driven Development (TDD): 
# write test -> fails (red) -> make it pass (green) -> make it better

# (pgbackup-E7nj_BsO) pgbackup $  
# (pgbackup-E7nj_BsO) pgbackup $ vim tests/test_cli.py
================================================================================
import pytest

from pgbackup import cli

url = "postgres://bob:password@example.com:1234/db_one"

def test_parser_without_driver():
    # without a specified driver the parser will exit and return an error
    with pytest.rasies(SystemExit):
        parser = cli.create_parser()
        parser.parse_arges([url])

# https://docs.pytest.org/en/latest/
================================================================================
# :wq
(pgbackup-E7nj_BsO) pgbackup $ make
PYTHONPATH=./src pytest
/bin/sh: pytest: command not found
make: *** [test] Error 127


# Looks like we do not have pytest installed in our pipenv
# (pgbackup-E7nj_BsO) pgbackup $
# (pgbackup-E7nj_BsO) pgbackup $ pipenv install --dev pytest
# (pgbackup-E7nj_BsO) pgbackup $
# (pgbackup-E7nj_BsO) pgbackup $ make
PYTHONPATH=./src pytest
============================ test session starts ===============================
platform linux2 -- Python 2.7.5, pytest-3.4.0, py-1.5.2, pluggy-0.6.0
rootdir: /home/user/code/pgbackup, inifile:
collected 0 items / 1 errors                                                                                                             
================================= ERRORS =======================================
____________________ ERROR collecting tests/test_cli.py ______________________
ImportError while importing test module '/home/user/code/pgbackup/tests/test_cli.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
tests/test_cli.py:3: in <module>
    from pgbackup import cli
E   ImportError: cannot import name cli
!!!!!!!!!!!!!! Interrupted: 1 errors during collection !!!!!!!!!!!!!!!!!!!!!!!
======================== 1 error in 0.09 seconds ===============================
make: *** [test] Error 2


# Looks like we do not have a cli module either!
# Make a blank cli module within the package
# (pgbackup-E7nj_BsO) pgbackup $
# (pgbackup-E7nj_BsO) pgbackup $ vim src/pgbackup/cli.py
# (pgbackup-E7nj_BsO) pgbackup $
# (pgbackup-E7nj_BsO) pgbackup $ make
PYTHONPATH=./src pytest
============================== test session starts =============================
platform linux2 -- Python 2.7.5, pytest-3.4.0, py-1.5.2, pluggy-0.6.0
rootdir: /home/user/code/pgbackup, inifile:
collected 1 item                                                                                                                         
tests/test_cli.py F                                                                                                                
==================================== FAILURES ==================================
____________________________ test_parser_without_driver ________________________
    def test_parser_without_driver():
        """
        Without a specified driver the parser will exit
        """
        with pytest.raises(SystemExit):
>       parser = cli.create_parser()
E    AttributeError: 'module' object has no attribute 'create_parser'
tests/test_cli.py:12: AttributeError
============================== 1 failed in 0.03 seconds ========================
make: *** [test] Error 1


# (pgbackup-E7nj_BsO) pgbackup $
# (pgbackup-E7nj_BsO) pgbackup $ vim src/pgbackup/cli.py
================================================================================
import argparse

def create_parser():
	parser = argparse.ArgumentParser(description="""
	Backup PostgreSQL databases to AWS S3 or locally.
	""")
    return parser

================================================================================
#:wq
# You get the idea :)