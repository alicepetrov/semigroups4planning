"""
"""
import sys

import numpy as np


class TransformationSemigroup():
    """
    """
    def __init__(
        self,
        actions
    ):
        self._actions = actions
        self._generators = [v for v in actions.values()]
        self._generators_as_string = [np.array2string(v, separator=', ', max_line_width=sys.maxsize) for v in self._generators]


    def get_transformation_kernel(): # TODO
        pass

    def get_transformation_image(): # TODO
        pass

    def get_transformation_rank(): # TODO
        pass
