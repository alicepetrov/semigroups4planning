"""
"""
from jinja2 import Environment, FileSystemLoader
import os
import sys
import numpy as np

from . import HERE

class GAP():
    """
    """
    def __init__(
        self,
        folder,
        packages
    ):
        self._folder = folder
        self._packages = packages
        self._environment = Environment(loader=FileSystemLoader(os.path.join(HERE, "templates/")))

    
    def create_transformation_semigroup(self, generators, var: str = "S"):
        """
        """
        transformations = [np.array2string(v, separator=', ', max_line_width=sys.maxsize) for v in generators]
        
        template = self._environment.get_template("transformation_semigroup.txt")
        content = template.render(var = var, generators = transformations)

        # with open("test.txt", mode="w", encoding="utf-8") as message: # TODO remove after testing
        #     message.write(content)
        