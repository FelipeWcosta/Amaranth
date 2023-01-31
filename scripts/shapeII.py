from amaranth import *
import enum
class Direction(enum.Enum):
    TOP = 0
    LEFT = 1
    BOTTOM = 2
    RIGHT = 3
print(Shape.cast(Direction))
print(Value.cast(5))
print(Value.cast(Direction.LEFT))