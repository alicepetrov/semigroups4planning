"""
Functions for converting PDDL to Semigroups
"""
# Imports
import networkx as nx
import numpy as np
from macq.generate.pddl import StateEnumerator

from .semigroup import TransformationSemigroup


def generate_state_space(
    domain: str, 
    problem: str, 
    relabel: bool = True, 
    start_state: int = None,
    goal_state: int = None
    ):
    """Generates the entire state space of a PDDL problem and domain

    Keyword arguments:
    domain -- domain .pddl file 
    problem -- problem .pddl file
    relabel -- relabel the states with numbers?
    start_state -- add a dummy start state to our graph
    goal_state -- add a dummy goal state to our graph

    Returns:
    state_graph -- networkx graph
    """
    generator = StateEnumerator(dom=domain, prob=problem)

    # Get networkx graph
    graph = generator.graph

    # Identify start state
    if start_state:
        init_state = generator.problem.init
        graph.nodes[init_state]["name"] = "initial_state"

        # Add dummy transition
        graph.add_node(0, name="start")
        graph.add_edge(0, init_state, label="start_transition")

    # Identify goal state(s)
    if goal_state:
        goal = generator.problem.goal     

    if relabel:
        
        if goal_state:              
            # Counter to track number of states matching goal
            n = 1
            num_states = graph.number_of_nodes()
            # Identify states matching goal
            for state in list(graph):
                if not type(state) == int and state[goal]:
                    # Relabel
                    graph.nodes[state]["name"] = "goal"
                    graph.nodes[state]["goal_number"] = n

                    # Add dummy transition
                    graph.add_node(num_states, name="end")
                    graph.add_edge(state, num_states, label="end_transition")

                    # Increment counters
                    num_states += 1
                    n += 1

        # Relabel the states with numbers
        states = graph.nodes()
        state_mapping = dict(zip(states, range(len(states))))
        graph = nx.relabel_nodes(graph, state_mapping, copy=False)

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
    start_state: bool = True,
    goal_state: bool = True,
    add_sink: bool = True,
    add_identity: bool = True
    ):
    """Convert a PDDL problem and domain to a semigroup

    Keyword arguments:
    domain -- domain .pddl file 
    problem -- problem .pddl file
    relabel -- relabel the states with numbers?
    start_state -- add a dummy start state to our graph
    goal_state -- add a dummy goal state to our graph
    add sink -- use a sink state?
    add identity -- add an identity transformation?
    """
    # Get entire state space as networkx graph
    state_space = generate_state_space( 
        domain, 
        problem, 
        relabel, 
        start_state, 
        goal_state
        )
    # Extract transformations from graph
    transformations = digraph_to_transformations(state_space, add_sink, add_identity)

    # GAP indexes starting at 1
    for k , v in transformations.items(): transformations[k] = v + 1
    # Generate corresponding semigroup
    semigroup = TransformationSemigroup(transformations)

    return semigroup
