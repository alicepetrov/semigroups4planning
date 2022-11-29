# Imports
from argparse import ArgumentParser
import logging
import sys
from .__version__ import __version__

MESSAGE = """
                                                                             
█▀ █▀▀ █▀▄▀█ █ █▀▀ █▀█ █▀█ █░█ █▀█ █▀ ▄▄ █░█ ▄▄ █▀█ █░░ ▄▀█ █▄░█ █▄░█ █ █▄░█ █▀▀
▄█ ██▄ █░▀░█ █ █▄█ █▀▄ █▄█ █▄█ █▀▀ ▄█ ░░ ▀▀█ ░░ █▀▀ █▄▄ █▀█ █░▀█ █░▀█ █ █░▀█ █▄█
"""

class S4PParser(object):
    """
    """
    def __init__(self):
        
        print(MESSAGE)

        self._parser = ArgumentParser(
            prog="semigroups4planning"
        )
        
        self._supported_inputs = [
            "pddl",
        ]

        self._add_arguments()


    def _add_arguments(self):
        """
        """
        # Debugging for developers
        self._parser.add_argument(
            '-d', '--debug',
            help="Enable debugging statements",
            action="store_const", dest="loglevel", const=logging.DEBUG,
            default=logging.WARNING,
        )

        # Verbose logging for users
        self._parser.add_argument(
            '-v', '--verbose',
            help="Enable verbose logging",
            action="store_const", dest="loglevel", const=logging.INFO,
        )


    def error(self): # TODO
        print("Semigroups4Planning v" + __version__)
        self._parser.print_help()
        sys.exit(0)


    def parse_arguments(self):
        return self._parser.parse_args()
