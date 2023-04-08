# semigroups4planning

The following library converts classical planning domains and problems into semigroups, and then runs GAP functions to analyze them.
For best results, run from the provided Docker container.

## Installation

Navigate to root directory and run:
> pip install -r requirements.txt
> pip install .

## CLI Tool Usage

Usage:
> python3 -m semigroups4planning --domain_file <your_domain_file.pddl> --problem_file <your_problem_file.pddl> <function_to_run>

The <function_to_run> argument can be one of the following:
{get_basic_attributes, get_size, get_greens_relations, get_right_cayley_graph, get_subgroups}

options:
  -h, --help                        show this help message and exit
  -d, --debug                       Enable debugging statements
  -v, --verbose                     Enable verbose logging
  --domain_file DOMAIN              Specify the domain file
  --problem_file PROBLEM            Specify the problem file
  --relabel, --no-relabel           Relabel the states with numbers (default: True)
  --start_state, --no-start_state   Add a start state to graph (default: True)
  --goal_state, --no-goal_state     Add goal states to graph (default: True)
  --sink_state, --no-sink_state     Add sink state to graph (default: True)
  --identity, --no-identity         Add an identity transformation (default: True)

  Note that GAP scripts are saved in the gap_scripts folder.