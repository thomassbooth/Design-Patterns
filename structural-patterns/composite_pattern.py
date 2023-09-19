
from abc import ABC, abstractmethod

# Define the interface for graphic shapes
class IGraphicShape(ABC):

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def resize(self, width: float, height: float):
        pass


# Define the composite class for groups of shapes
class ShapeGroup(IGraphicShape):

    def __init__(self):
        # Initialize an empty list to hold shapes (individual shapes or other groups)
        self.shapes = []

    def add(self, shape: IGraphicShape):
        # Add a shape (individual shape or group) to this group
        self.shapes.append(shape)

    def render(self):
        # Render all shapes within this group
        for shape in self.shapes:
            shape.render()

    def resize(self, width: float, height: float):
        # Resize all shapes within this group
        for shape in self.shapes:
            shape.resize(width, height)


# Define a concrete class for circles
class Circle(IGraphicShape):

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def render(self):
        # Render the circle with its current width and height
        print(f'Rendering a circle of width: {self.width} and height: {self.height}')

    def resize(self, width: float, height: float):
        # Resize the circle to the specified width and height
        self.width = width
        self.height = height


def client_code():

    # Create a group to hold shapes
    shapes = ShapeGroup()

    # Create an individual circle and add it to the group
    circle = Circle(1, 2)
    shapes.add(circle)

    # Create a subgroup of circles and add it to the group
    circlesOfSize10 = ShapeGroup()
    circlesOfSize10.add(Circle(10, 10))
    shapes.add(circlesOfSize10)

    # Render all shapes within the group
    shapes.render()


if __name__ == '__main__':
    client_code()
