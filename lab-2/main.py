import math

class Vector:
    def __init__(self, *args):
        self.values = args

    def norm(self):
        return math.sqrt(sum(i**2 for i in self.values))

    def __add__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Both vectors must have the same number of elements")
        return Vector(*(x + y for x, y in zip(self.values, other.values)))

    def __sub__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Both vectors must have the same number of elements")
        return Vector(*(x - y for x, y in zip(self.values, other.values)))

    def __mul__(self, scalar):
        return Vector(*(x * scalar for x in self.values))

    def __truediv__(self, scalar):
        return Vector(*(x / scalar for x in self.values))

    def dot(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("Both vectors must have the same number of elements")
        return sum(x * y for x, y in zip(self.values, other.values))

    def cross(self, other):
        if len(self.values) != 3 or len(other.values) != 3:
            raise ValueError("Both vectors must have 3 elements")
        return Vector(
            self.values[1] * other.values[2] - self.values[2] * other.values[1],
            self.values[2] * other.values[0] - self.values[0] * other.values[2],
            self.values[0] * other.values[1] - self.values[1] * other.values[0]
        )


v1 = Vector(1, 2, 3)
print(v1.norm())
v2 = Vector(2, 3, 4)
v3 = v1 + v2
print(v3.values) # Output: (3, 5, 7)

v3 = v1 - v2
print(v3.values) # Output: (-1, -1, -1)

v2 = v1 * 2
print(v2.values) # Output: (2, 4, 6)

v2 = v1 / 2
print(v2.values) # Output: (0.5, 1.0, 1.5)


v1 = Vector(1, 2, 3)
v2 = Vector(2, 3, 4)
result = v1.dot(v2)
print(result) # Output: 20

v3 = v1.cross(v2)
print(v3.values) # Output: (-1, 2, -1)
