from dataclasses import dataclass, field
from math import sqrt, cos, sin, radians, isclose
from functools import lru_cache

class InvalidPositionError(Exception):
    pass

@dataclass(frozen=True)
class Position:
    x: float = field(metadata={'type': (int, float)})
    y: float = field(metadata={'type': (int, float)})

    def __post_init__(self):
        if not isinstance(self.x, (int, float)) or not isinstance(self.y, (int, float)):
            raise InvalidPositionError(f"Coordinates must be numeric, got x: {type(self.x).__name__}, y: {type(self.y).__name__}.")

    @lru_cache(maxsize=None)
    def move(self, angle: 'Degrees', steps: int) -> 'Position':
        rad_angle = radians(angle.angle)
        dx = steps * cos(rad_angle)
        dy = steps * sin(rad_angle)
        return Position(self.x + dx, self.y + dy)

    def distance_to(self, other: 'Position') -> float:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def is_in(self, top_left: 'Position', bottom_right: 'Position') -> bool:
        return (top_left.x <= self.x <= bottom_right.x and
                bottom_right.y <= self.y <= top_left.y)

    def __add__(self, other: 'Position') -> 'Position':
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Position') -> 'Position':
        return Position(self.x - other.x, self.y - other.y)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Position):
            return NotImplemented
        return isclose(self.x, other.x, abs_tol=1e-9) and isclose(self.y, other.y, abs_tol=1e-9)

    def __repr__(self):
        return f"Position(x={self.x}, y={self.y})"

    def __str__(self) -> str:
        return f"({self._format_value(self.x)}, {self._format_value(self.y)})"

    @staticmethod
    def _format_value(value: float) -> str:
        if abs(value - round(value)) < 1e-6:
            return f"{round(value)}"
        else:
            return f"{value:.6f}"
