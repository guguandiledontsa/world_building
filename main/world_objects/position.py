from dataclasses import dataclass
from math import sqrt, cos, sin, radians, isclose


class InvalidPositionError(Exception):
    """Custom exception for invalid position input."""
    pass


class PositionCache:
    _cache = {}

    @classmethod
    def get_position(cls, x: float, y: float) -> 'Position':
        key = (round(x, 6), round(y, 6))  # Round for cache key
        if key not in cls._cache:
            cls._cache[key] = Position(x, y)
        return cls._cache[key]

@dataclass(frozen=True)
class Position:
    x: float
    y: float

    def __post_init__(self):
        if not isinstance(self.x, (int, float)) or not isinstance(self.y, (int, float)):
            raise InvalidPositionError(f"Coordinates must be numeric, got x: {type(self.x).__name__}, y: {type(self.y).__name__}.")

    def move(self, angle: 'Degrees', steps: int) -> 'Position':
        rad_angle = radians(angle.angle)
        dx = steps * cos(rad_angle)
        dy = steps * sin(rad_angle)
        return PositionCache.get_position(self.x + dx, self.y + dy)

    def distance_to(self, other: 'Position') -> float:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def is_in(self, top_left: 'Position', bottom_right: 'Position') -> bool:
        return (top_left.x <= self.x <= bottom_right.x and
                bottom_right.y <= self.y <= top_left.y)

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
