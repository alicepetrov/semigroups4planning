"""
Command Line Interface
"""
import logging

from .arg_parser import S4PParser


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

    # python -m semigroups4planning

    from .convert import pddl_to_semigroup

    domain = "examples/drive-mini/domain.pddl"
    problem = "examples/drive-mini/problem.pddl"

    test_sg = pddl_to_semigroup(
        domain, 
        problem,
        relabel = True, 
        add_sink = True,
        add_identity = True
        )

    from .gap import GAP

    gap = GAP() # TODO

    gap.get_basic_attributes(test_sg)

    # -------------------------------------------------------------------------


if __name__ == '__main__':
    main()