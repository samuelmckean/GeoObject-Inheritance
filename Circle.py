# import all data fields and methods from superclass
from GeometricObject import GeometricObject 
import math

class Circle(GeometricObject):
    # construct a circle object
    def __init__(self, radius=1):
        super().__init__()
        self.__radius = radius

    def __str__(self):
        return super().__str__() + " radius: " + str(self.__radius)

    def getRadius(self):
        return self.__radius

    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    def getArea(self):
        return self.__radius ** 2 * math.pi

    def setRadius(self, radius):
        self.__radius = radius

    def getDiameter(self):
        return 2 * self.__radius

    def printCircle(self):
        print(self.__str__() + "radius: " + str(self.__radius))
