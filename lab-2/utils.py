import numpy as np

class Vector:
    def __init__(self, *args):
        self.values = np.array(args)

    def norm(self):
        return np.linalg.norm(self.values)

    def __add__(self, other):
        if self.values.shape != other.values.shape:
            raise ValueError("Both vectors must have the same number of elements")
        return Vector(*(self.values + other.values))

    def __sub__(self, other):
        if self.values.shape != other.values.shape:
            raise ValueError("Both vectors must have the same number of elements")
        return Vector(*(self.values - other.values))

    def __mul__(self, scalar):
        return Vector(*(self.values * scalar))

    def __truediv__(self, scalar):
        return Vector(*(self.values / scalar))

    def dot(self, other):
        if self.values.shape != other.values.shape:
            raise ValueError("Both vectors must have the same number of elements")
        return np.dot(self.values, other.values)

    def cross(self, other):
        if self.values.shape != (3,) or other.values.shape != (3,):
            raise ValueError("Both vectors must have 3 elements")
        return Vector(*np.cross(self.values, other.values))



# v1 = Vector(1, 2, 3)
# print("norm: ",v1.norm())
# v2 = Vector(2, 3, 4)
# v3 = v1 + v2
# print("addition: ", v3.values) # Output: (3, 5, 7)

# v3 = v1 - v2
# print("substraction: ",v3.values) # Output: (-1, -1, -1)

# v2 = v1 * 2
# print("multiplication: ",v2.values) # Output: (2, 4, 6)

# v2 = v1 / 2
# print("div: ",v2.values) # Output: (0.5, 1.0, 1.5)

# result = v1.dot(v2)
# print("dot: ",result) # Output: 20

# v3 = v1.cross(v2)
# print("cross: ",v3.values) # Output: (-1, 2, -1)

# print("v1: Vector(1, 2, 3)")
# print("v2: Vector(2, 3, 4)")
