# Constructor is always __init__ and doesn't return a value
# First argument of methods is always the called instance self
# We say what arguments are expected in the __init__ method
# _className is a protected method
import math
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def length(self):
        # return math.sqrt(self.x**2 + self.y**2)
        return sum(_ ** 2 for _ in self._coords()) ** 0.5
    def _coords(self):
        return (self.x, self.y, self.z)
    # Mutation method
    def normalize(self):
        length = self.length()
        self.x /= length
        self.y /= length
        self.z /= length
    # Non-mutating method
    def normalized(self):
        length = self.length()
        return Vector(self.x / length,
        self.y / length, self.z / length)
    def __eq__(self, other):
        return self._coords == other._coords
    # Static method
    @staticmethod
    def from_list(numbers):
        if len(numbers) != 3:
            print("Error")
        return Vector(numbers[0],numbers[1],numbers[2])
spam=Vector(1.0, 1.0, 1.0)
print(spam.x)
print(spam.length())
v=Vector.from_list([1,2,3])

class Stamp:
    def __init__(self, name):
        self.name = name
    def __call__(self, something):
        print(f"{something} was stamped by {self.name}")

#That thing there was stamped by The government
stamp=Stamp("The government")
stamp("That thing there")

print(getattr(spam,'x'))
setattr(spam,'z',5)
print(getattr(spam,'z'))

class Countable:
    _count = 0

    def __init__(self, data):
        self.data = data
        type(self).increase_count()
    @classmethod
    def increase_count(cls):
        cls._count +=1
    @classmethod
    def decrease_count(cls):
        cls._count -=1
    # Destructor
    def __del__(self):
        type(self).decrease_count()

class TwoCoordsVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # The method acts like property
    @property
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)
    def _coords(self):
        return (self.x, self.y)

spam = TwoCoordsVector(1.0, 2.0)
print(spam.length)

class Color:
    def __init__(self, rgba):
        self._rgba = tuple(rgba)
    @property
    def rgba(self):
        return self._rgba
    # This way we can change a property
    @rgba.setter
    def rgba(self, value):
        self._rgba = tuple(value)

red = Color([255,0,0])
print(red.rgba)
red.rgba=[127,0,0]
print(red.rgba)

def addition(a, b):
    return Vector(a.x + b.x, a.y + b.y, a.z + b.z)
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    __add__ = addition

print(Vector(1.0, 2.0, 3.0) + Vector(4.0, 5.0, 6.0))