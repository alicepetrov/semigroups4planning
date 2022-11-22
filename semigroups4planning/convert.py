"""
Functions for converting PDDL to Semigroups
"""
# Imports
from macq.generate.pddl import StateEnumerator
import networkx as nx
import numpy as np
from semigroups import TransformationSemigroup


def generate_state_space(
    domain: str, 
    problem: str, 
    relabel: bool = True, 
    start_action: bool = True,
    end_action: bool = True
    ):
    """Generates the entire state space of a PDDL problem and domain

    Keyword arguments:
    domain -- domain .pddl file 
    problem -- problem .pddl file
    relabel -- relabel the states with numbers?
    start_action -- add a dummy start action to our initial state?
    end_action -- add a dummy end ection to our goal state?

    Returns:
    state_graph -- networkx graph
    """
    generator = StateEnumerator(dom=domain, prob=problem)

    # Get networkx graph
    graph = generator.graph

    # Optionally add start transition
    if start_action:
        pass # TODO

    # Optionally add end transition
    if end_action:
        pass # TODO

    if relabel:
        # Get states
        states = list(graph.nodes())
        # Relabel the states with numbers
        state_mapping = dict(zip(states, range(len(states))))
        graph = nx.relabel_nodes(graph, state_mapping)

    return graph


def digraph_to_transformations(
    digraph: nx.graph, 
    actions: list(str), 
    add_sink: bool = True, 
    add_identity: bool = True
    ):
    """Convert a NetworkX Digraph to a set of Transformations

    Keyword arguments:
    digraph -- networkX graph encoding state space
    actions -- list of actions
    add sink -- use a sink state?
    add identity -- add an identity transformation?
    """
    # Add an identity transformation
    if add_identity: actions.append("identity")
    # Create index to keep track of actions in np array
    action_index = {k: v for v, k in enumerate(actions)}
    # Get number of actions
    num_actions = len(actions)

    # Set up states
    num_states = digraph.number_of_nodes()

    if add_sink:
        # Send every state to the sink
        transformations = np.full((num_actions, num_states+1), num_states+1)
    else:
        # Send every state to itself
        identity = np.arange(num_states)
        transformations = np.tile(identity,(num_actions,1))

    # TODO Iterate through graph and update transformations

    # TODO Convert transformations to Transformation objects


def pddl_to_semigroup(
    domain: str, 
    problem: str,
    relabel: bool = True, 
    start_action: bool = True,
    end_action: bool = True,
    add_sink: bool = True,
    add_identity: bool = True
    ):
    """Convert a PDDL problem and domain to a semigroup

    Keyword arguments:
    domain -- domain .pddl file 
    problem -- problem .pddl file
    relabel -- relabel the states with numbers?
    start_action -- add a dummy start action to our initial state?
    end_action -- add a dummy end ection to our goal state?
    add sink -- use a sink state?
    add identity -- add an identity transformation?
    """
    # Read PDDL
    actions = [] # TODO

    # Get entire state space as networkx graph
    state_space = generate_state_space( 
        domain, 
        problem, 
        relabel, 
        start_action, 
        end_action
        ) # TODO kwargs?

    # Extract transformations from graph
    generators = digraph_to_transformations(state_space, actions, add_sink, add_identity)

    # Generate corresponding semigroup
    semigroup = TransformationSemigroup(generators)
