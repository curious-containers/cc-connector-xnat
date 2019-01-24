from cc_connector_cli.connector_cli import run_connector
from red_connector_xnat.http import Http


def main():
    run_connector(Http)
