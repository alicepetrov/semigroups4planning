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

    
    def create_transformation_semigroup(self, generators, transformation_semigroup: str = "S"):
        """
        """
        transformations = [np.array2string(v, separator=', ', max_line_width=sys.maxsize) for v in generators]
        
        template = self._environment.get_template("functions/transformation_semigroup.txt")
        content = template.render(transformation_semigroup = transformation_semigroup, generators = transformations)

        # TODO call GAP with content

        # with open("test.txt", mode="w", encoding="utf-8") as message: # TODO remove after testing
        #     message.write(content)

    def get_basic_attributes(self, generators, transformation_semigroup: str = "S"):
        """
        """
        transformations = [np.array2string(v, separator=', ', max_line_width=sys.maxsize) for v in generators]
        
        template = self._environment.get_template("basic_attributes.txt")
        content = template.render(transformation_semigroup = transformation_semigroup, generators = transformations)
        