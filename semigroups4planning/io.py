"""
"""
# Imports
from macq.generate.pddl import planning_domains_api
from tarski.io import PDDLReader
import requests


def read_pddl(problem_id: int = None, problem: str = None, domain: str = None):
    """Read and parse a PDDL problem and/or domain

    Keyword arguments:
        problem_id -- The ID of the problem to access
        problem -- The problem filename
        domain -- The domain filename          
    """
    reader = PDDLReader(raise_on_error=True)

    dom, prob = None

    if problem_id or problem:
        prob = read_problem(reader, problem_id, problem)

    if problem_id or domain:
        dom = read_domain(reader, problem_id, domain)

    return {"problem": prob, "domain": dom}


def read_domain(reader: PDDLReader, problem_id: int = None, domain: str = None):
    """Parse a PDDL domain

    Keyword arguments:
        reader -- a tarski PDDLReader
        problem_id -- The ID of the problem to access
        domain -- The domain filename       
    """
    if not problem_id:
        return reader.parse_domain(domain)
    else:
        dom = requests.get(planning_domains_api.get_problem(problem_id)["domain_url"]).text
        return reader.parse_domain_string(dom)


def read_problem(reader: PDDLReader, problem_id: int = None, problem: str = None):
    """Parse a PDDL problem

    Keyword arguments:
        reader -- a tarski PDDLReader
        problem_id -- The ID of the problem to access
        problem -- The problem filename  
    """
    if not problem_id:
        return reader.parse_instance(problem)
    else:
        prob = requests.get(planning_domains_api.get_problem(problem_id)["problem_url"]).text
        return reader.parse_instance_string(prob)
