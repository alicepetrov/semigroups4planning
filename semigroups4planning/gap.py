"""
GAP class for building and executing scripts
"""
import os

from jinja2 import Environment, FileSystemLoader

from . import HERE
from .file_helpers import safe_open_w, save_dot_as_img


class GAP():
    """
    """
    def __init__(
        self
    ):
        self._environment = Environment(loader=FileSystemLoader(os.path.join(HERE, "templates/")))


    def execute_script(self, filename: str):
        """Execute a GAP file as a bash script

        Keyword arguments:
            filename -- GAP file to read
        """
        # Generate bash script
        template = self._environment.get_template("execute_gap_script.txt")
        content = template.render(file = filename)

        # Execute bash script
        os.system(content)
    
    
    def create_transformation_semigroup(self, semigroup):
        """Template to declare a transformation semigroup

        Keyword arguments:
            semigroup -- TransformationSemigroup object
        """
        # Generate GAP script
        template = self._environment.get_template("functions/transformation_semigroup.txt")
        content = template.render(generators = semigroup._generators_as_string)

        # Save GAP script
        filename = "gap_scripts/create_transformation_semigroup.g"
        with safe_open_w(filename) as f:
            f.write(content)

        # Execute as bash script
        self.execute_script(filename)

    
    def get_size(self, semigroup):
        """Template to get size of a transformation semigroup

        Keyword arguments:
            semigroup -- TransformationSemigroup object
        """
        # Generate GAP script
        template = self._environment.get_template("get_size.txt")
        content = template.render(generators = semigroup._generators_as_string)

        # Save GAP script
        filename = "gap_scripts/get_size.g"
        with safe_open_w(filename) as f:
            f.write(content)

        # Execute as bash script
        self.execute_script(filename)


    def get_basic_attributes(self, semigroup):
        """Template to get basic properties, digraph, etc of a transformation semigroup

        Keyword arguments:
            semigroup -- TransformationSemigroup object
        """
        # Generate GAP script
        template = self._environment.get_template("basic_attributes.txt")
        content = template.render(generators = semigroup._generators_as_string)

        # Save GAP script
        filename = "gap_scripts/get_basic_attributes.g"
        with safe_open_w(filename) as f:
            f.write(content)

        # Execute as bash script
        self.execute_script(filename)

        # Save DOT as image
        save_dot_as_img("dot_drawing_actions_on_points.dot")

    
    def get_greens_relations(self, semigroup):
        """Template to get Green's Classes of a transformation semigroup

        Keyword arguments:
            semigroup -- TransformationSemigroup object
        """
        # Generate GAP script
        template = self._environment.get_template("greens_relations.txt")
        content = template.render(generators = semigroup._generators_as_string)

        # Save GAP script
        filename = "gap_scripts/get_greens_relations.g"
        with safe_open_w(filename) as f:
            f.write(content)

        # Execute as bash script
        self.execute_script(filename)

        # Save DOT as image
        save_dot_as_img("dot_for_drawing_d_classes.dot")
  