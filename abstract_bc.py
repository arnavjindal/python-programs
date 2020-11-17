
# from abc import ABCMeta, abstractmethod    <-----------------------------------FOR PYTHON 3.4 BELOW
from abc import ABC, abstractmethod         # THIS IS GOOD TO GO FOR LATEST PYTHON WALE!!

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())
#AB= Shape()  YOU CAN'T MAKE A INSTANCE IN AN ABSTRACT CLASS
