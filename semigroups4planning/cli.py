"""
Command Line Interface
"""
import logging

from .arg_parser import S4PParser
from .convert import pddl_to_semigroup

# Set up parser and arguments
PARSER = S4PParser()
ARGS = PARSER.parse_arguments()

# Set up logging           
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(ARGS.loglevel)

def main():
    """
    """
    semigroup = pddl_to_semigroup(
        ARGS.domain, 
        ARGS.problem,
        relabel = ARGS.relabel, 
        start_state = ARGS.start_state, 
        goal_state = ARGS.goal_state, 
        add_sink = ARGS.sink_state,
        add_identity = ARGS.identity
        )

    # Identify which script to run
    func = PARSER._functions[ARGS.command]
    func(semigroup)

if __name__ == '__main__':
    main()