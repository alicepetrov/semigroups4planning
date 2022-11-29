"""
"""
# TODO datatypes

class Transformation():
    def __init__(
        self,
        name,
        transformation
    ):
        self._name = name
        self._transformation = transformation
        self._kernel = self.get_kernel(transformation)
        self._image = self.get_image(transformation)


    def get_kernel(): # TODO
        pass

    def get_image(): # TODO
        pass

    def get_rank(): # TODO (Should this be an attribute?)
        pass


class TransformationSemigroup():
    """
    """
    def __init__(
        self, 
        generators
    ):
        self._generators = generators


    def build(self): # TODO
        pass