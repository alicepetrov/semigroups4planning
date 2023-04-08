"""
Argument parser for CLI tool
"""
import logging
import sys
import argparse
from .gap import GAP

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

        self._parser = argparse.ArgumentParser(
            prog="semigroups4planning"
        )
        
        self._supported_inputs = [
            "pddl",
        ]

        gap = GAP()

        self._functions = {
            'get_basic_attributes' : gap.get_basic_attributes,
            'get_size' : gap.get_size,
            'get_greens_relations': gap.get_greens_relations,
            'get_right_cayley_graph': gap.get_right_cayley_graph,
            'get_subgroups': gap.get_subgroups
            }

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

        # Domain file
        self._parser.add_argument(
            '--domain_file',
            help="Specify the domain file",
            dest="domain"
        )

        # Problem file
        self._parser.add_argument(
            '--problem_file',
            help="Specify the problem file",
            dest="problem"
        )

        # Relabel the states with numbers
        self._parser.add_argument(
            '--relabel',
            help="Relabel the states with numbers",
            dest="relabel",
            action=argparse.BooleanOptionalAction,
            default=True,
        )

        # Add a start state
        self._parser.add_argument(
            '--start_state',
            help="Add a start state to graph",
            dest="start_state",
            action=argparse.BooleanOptionalAction,
            default=True,
        )

        # Add goal states
        self._parser.add_argument(
            '--goal_state',
            help="Add goal states to graph",
            dest="goal_state",
            action=argparse.BooleanOptionalAction,
            default=True,
        )

        # Add sink state
        self._parser.add_argument(
            '--sink_state',
            help="Add sink state to graph",
            dest="sink_state",
            action=argparse.BooleanOptionalAction,
            default=True,
        )

        # Add an identity transformation
        self._parser.add_argument(
            '--identity',
            help="Add an identity transformation",
            dest="identity",
            action=argparse.BooleanOptionalAction,
            default=True,
        )

        self._parser.add_argument(
            'command', 
            choices=self._functions.keys()
            )


    def error(self): # TODO
        print("Semigroups4Planning v" + __version__)
        self._parser.print_help()
        sys.exit(0)


    def parse_arguments(self):
        return self._parser.parse_args()
