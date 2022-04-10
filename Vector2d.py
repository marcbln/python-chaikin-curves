import math

class Vector2d(object):
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def getLength(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalized(self) -> "Vector2d":
        """ Returns new normalized vector """
        length = self.getLength()
        return Vector2d(self.x / length, self.y / length)

    def normalize_(self) -> None:
        """
        the "_" at the end of the function name is to show that the Vector2d gets modified (like "!" in ruby)
        """
        l = self.length()
        self.x /= l
        self.y /= l

    def rotated(self, thetaDeg) -> "Vector2d":
        """ return rotated vector (counter clockwise) """
        theta = math.radians(thetaDeg)
        dc = math.cos(theta)
        ds = math.sin(theta)
        x = dc * self.x - ds * self.y
        y = ds * self.x + dc * self.y
        return Vector2d(x, y)

    def perpendicularCounterClockwise(self) -> "Vector2d":
        return Vector2d(self.y, -self.x)

    def perpendicularClockwise(self) -> "Vector2d":
        return Vector2d(-self.y, self.x)

    def __mul__(self, factor: float) -> "Vector2d":
        """ multiply with int/float """
        return Vector2d(self.x * factor, self.y * factor)

    def __truediv__(self, divisor: float) -> "Vector2d":
        """ divide with int/float """
        return self.__mul__(1.0 / divisor)

    def __sub__(self, other: "Vector2d") -> "Vector2d":
        return Vector2d(self.x - other.x, self.y - other.y)

    def __add__(self, other: "Vector2d") -> "Vector2d":
        return Vector2d(self.x + other.x, self.y + other.y)

    def __eq__(self, other: "Vector2d") -> bool:
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return "(%.2f %.2f)" % (self.x, self.y)

    __radd__ = __add__
    __rmul__ = __mul__

    def asIntTuple(self):
        # TODO: rename asIntTupleRound() + add methods asIntTuple{Ceil/Floor}
        return (int(round(self.x)), int(round(self.y)))

    def asTuple(self):
        return (self.x, self.y)

    def getAngle(self, bDegrees=False):
        alpha = math.atan2(self.y, self.x)
        return (alpha  * 180 / math.pi) if bDegrees else alpha

    def distanceTo(self, other: "Vector2d") -> float:
        dx = other.x - self.x
        dy = other.y - self.y

        return math.sqrt(dx ** 2 + dy ** 2)

    def length(self) -> float: # TODO: same as getLength .. remove one of them
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def hasZeroLength(self, threshold: float = 1e-8):
        # to avoid floating point error
        return abs(self.x) < threshold and abs(self.y) < threshold

    def isNan(self) -> bool:
        return math.isnan(self.x) or math.isnan(self.y)

