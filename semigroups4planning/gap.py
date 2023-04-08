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
        """
        # Generate bash script
        template = self._environment.get_template("execute_gap_script.txt")
        content = template.render(file = filename)

        # Execute bash script
        os.system(content)


    def generate_script(self, semigroup, template_file: str, filename):
        """Write to GAP script
        """
        # Generate GAP script
        template = self._environment.get_template(template_file)
        content = template.render(generators = semigroup._generators_as_string)

        # Save GAP script
        with safe_open_w(filename) as f:
            f.write(content)
    
    
    def create_transformation_semigroup(self, semigroup):
        """Template to declare a transformation semigroup

        Keyword arguments:
            semigroup -- TransformationSemigroup object
        """
        # File names
        template_file = "functions/transformation_semigroup.txt"
        filename = "gap_scripts/create_transformation_semigroup.g"

        # Setup script
        self.generate__script(semigroup, template_file, filename)
        # Execute as bash script
        self.execute_script(filename)

    
    def get_size(self, semigroup):
        """Template to get size of a transformation semigroup

        Keyword arguments:
            semigroup -- TransformationSemigroup object
        """
        # File names
        template_file = "get_size.txt"
        filename = "gap_scripts/get_size.g"

        # Generate_ script
        self.generate_script(semigroup, template_file, filename)
        # Execute as bash script
        self.execute_script(filename)


    def get_basic_attributes(self, semigroup):
        """Template to get basic properties, digraph, etc of a transformation semigroup

        Keyword arguments:
            semigroup -- TransformationSemigroup object
        """
        # File names
        template_file = "basic_attributes.txt"
        filename = "gap_scripts/get_basic_attributes.g"

        # Generate_ script
        self.generate_script(semigroup, template_file, filename)
        # Execute as bash script
        self.execute_script(filename)

        # Save DOT as image
        save_dot_as_img("dot_drawing_actions_on_points.dot")

        # Save DOT as image
        save_dot_as_img("dot_for_drawing_d_classes.dot")

    
    def get_greens_relations(self, semigroup):
        """Template to get Green's Classes of a transformation semigroup

        Keyword arguments:
            semigroup -- TransformationSemigroup object
        """
        # File names
        template_file = "greens_relations.txt"
        filename = "gap_scripts/get_greens_relations.g"

        # Generate_ script
        self.generate_script(semigroup, template_file, filename)
        # Execute as bash script
        self.execute_script(filename)

        # Save DOT as image
        save_dot_as_img("dot_for_drawing_d_classes.dot")


    def get_right_cayley_graph(self, semigroup):
        """Template to get Right Cayley Graph of a transformation semigroup

        Keyword arguments:
            semigroup -- TransformationSemigroup object
        """
        # File names
        template_file = "right_cayley_graph.txt"
        filename = "gap_scripts/get_right_cayley_graph.g"

        # Generate_ script
        self.generate_script(semigroup, template_file, filename)
        # Execute as bash script
        self.execute_script(filename)

        # Save DOT as image
        save_dot_as_img("dot_drawing_right_cayley_graph.dot")

        # Save DOT as image
        save_dot_as_img("dot_drawing_right_cayley_automaton.dot")


    def get_subgroups(self, semigroup):
        """Template to get the subgroups of the semigroup

        Keyword arguments:
            semigroup -- TransformationSemigroup object
        """
        # File names
        template_file = "subgroups.txt"
        filename = "gap_scripts/get_subgroups.g"

        # Generate_ script
        self.generate_script(semigroup, template_file, filename)
        # Execute as bash script
        self.execute_script(filename)

        # Save DOT as image
        save_dot_as_img("d_classes_with_group_h_classes.dot")
  