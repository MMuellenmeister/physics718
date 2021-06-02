import math


class Vector2D:
    # class initialisation
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def copy(self):
        return Vector2D(self.x, self.y)

    def __str__(self):
        return (
            "x:" + str(self.x) + ", y:" + str(self.y)
        )  # Human-readable string representation of the vector.

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__str__()})"

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __mul__(self, other):  # dot product or multiplication by scalar
        if isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        if isinstance(other, (float, int)):
            return Vector2D(self.x * other, self.y * other)
        raise NotImplementedError(
            "Can only multiply Vector2D by a scalar or another Vector2D"
        )

    def __rmul__(
        self, other
    ):  # Reverse multiplication so that vector * scalar also works.
        return self.__mul__(other)

    def __truediv__(self, other):
        return Vector2D(self.x/other, self.y/other)

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self  # it is customary to have a return value for += operator

    # end of operators
    # class methods start here
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    __abs__ = magnitude

    def distance_to(self, other):
        return abs(self - other)

    def to_polar(self):
        return self.__abs__(), math.atan2(self.y, self.x)

    def normal(self):
        return self/self.magnitude()
    
    def angle_to(self, other):
        #  if isinstance(other, Vector2D):
        #      raise ValueError()
        return math.atan(self.y/self.x)+math.atan(other.y/other.x)