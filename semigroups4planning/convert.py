"""
Functions for converting PDDL to Semigroups
"""
# Imports
from macq.generate.pddl import StateEnumerator
import networkx as nx
import numpy as np
from .semigroups import TransformationSemigroup


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
    add_sink: bool = True, 
    add_identity: bool = True
    ):
    """Convert a NetworkX Digraph to a set of Transformations

    Keyword arguments:
    digraph -- networkX graph encoding state space
    add sink -- use a sink state?
    add identity -- add an identity transformation?
    """
    # Set up states
    num_states = digraph.number_of_nodes()

    if add_sink:
        # Send every state to the sink
        # i.e if num_states = 5, then [6, 6,...,6]
        num_states += 1
        init_transformation = np.full(num_states, num_states-1)
    else:
        # Send every state to itself
        # i.e [1, 2,...,n]
        init_transformation = np.arange(num_states)

    # Initialize dictionary to store transformations
    actions = {}

    # Add an identity transformation
    if add_identity: actions["identity"] = np.arange(num_states)

    # Iterate through graph and update transformations
    for u, v, act in digraph.edges(data=True):
        label = act['label']

        # Add new action if necessary
        if label not in actions:
            actions[label] = init_transformation.copy()

        actions[label][u] = v

    return actions


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
    # Get entire state space as networkx graph
    state_space = generate_state_space( 
        domain, 
        problem, 
        relabel, 
        start_action, 
        end_action
        ) # TODO kwargs?

    # Extract transformations from graph
    generators = digraph_to_transformations(state_space, add_sink, add_identity)

    # Generate corresponding semigroup
    semigroup = TransformationSemigroup(generators)
