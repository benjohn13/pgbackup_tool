# [pgbackup $]
# [pgbackup $] vim tests/test_cli.py

import pytest
from pgbackup import cli

url = "postgres://bob:password@example.com:1234/db_one"

def test_parser_without_driver():
    # without a specified driver the parser will exit and return an error
   parser = cli.create_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([url])

def test_parser_with_driver():
	"""
	The parser will exit if it receives a driver without a destination
	"""
	parser = cli.create_parser()
	with pytest.raises(SystemExit):
        parser.parse_args([url, '--driver', 'local'])

def test_parser_with_driver_and_destination():
	"""
	The parser will NOT exit if it receives a driver and destination
	"""
    parser = cli.create_parser()
    args = parser.parse_args([url, '--driver', 'local', '/some/path'])

    assert args.driver == 'local'
    assert args.destination = '/some/path'

# https://docs.pytest.org/en/latest/