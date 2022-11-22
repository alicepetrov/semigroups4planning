"""
"""
from .arg_parser import S4PParser
import logging

# Set up parser and arguments
PARSER = S4PParser()
ARGS = PARSER.parse_arguments()

# Set up logging
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(ARGS.loglevel)


def main():
    """
    """
    print(LOGGER.getEffectiveLevel())

if __name__ == '__main__':
    main()