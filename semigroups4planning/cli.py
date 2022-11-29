"""
"""
from .arg_parser import S4PParser
import logging


# Set up parser and arguments
PARSER = S4PParser()
ARGS = PARSER.parse_arguments()


# Set up logging, # TODO Set up colours            
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(ARGS.loglevel)


def main(): # TODO
    """
    """
    # -------------------------------------------------------------------------
    # TODO Remove after testing

    # python -m semigroups4planning -h

    from .convert import pddl_to_semigroup

    domain = "C:/Users/Alice/source/repos/semigroups4planning/semigroups4planning/domain.pddl"
    problem = "C:/Users/Alice/source/repos/semigroups4planning/semigroups4planning/problem.pddl"

    pddl_to_semigroup(
        domain, 
        problem,
        relabel = True, 
        start_action = False,
        end_action = False,
        add_sink = True,
        add_identity = True
        )
    # -------------------------------------------------------------------------


if __name__ == '__main__':
    main()