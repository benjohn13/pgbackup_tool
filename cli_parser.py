# (pgbackup-E7nj_BsO) [pgbackup $]
# (pgbackup-E7nj_BsO) [pgbackup $] vim tests/test_cli.py

import pytest
from pgbackup import cli

url = "postgres://bob:password@example.com:1234/db_one"


@pytest.fixture()
def parser():
    return cli.create_parser()


def test_parser_without_driver(parser):
    """
    Without a specified driver the parser will exit
    """
    parser = cli.create_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([url])


def test_parser_with_driver(parser):
    """
    The parser will exit if it receives a driver without a destination
    """
    parser = cli.create_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([url, '--driver', 'local'])


def test_parser_with_driver_and_destination(parser):
    """
    The parser will NOT exit if it receives a driver and destination
    """
    args = parser.parse_args([url, '--driver', 'local', '/some/path'])
    assert args.driver == 'local'
    assert args.destination == '/some/path'


def test_parser_with_unknown_driver(parser):
    """
    The parser will exit if the driver name is unknown.
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, '--driver', 'azure', 'destination'])


def test_parser_with_known_drivers(parser):
    """
    The parser will not exit if the driver name is known.
    """
    for driver in ['local', 's3']:
        assert parser.parse_args([url, '--driver', driver, 'destination'])


# https://docs.pytest.org/en/latest//
