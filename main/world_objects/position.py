from dataclasses import dataclass
from math import sqrt, isclose, cos, sin, radians
from functools import lru_cache
from typing import Union

from main.world_objects.degrees import Degrees


class InvalidPositionError(Exception):
    """Custom exception for invalid position coordinates."""
    pass


@dataclass(frozen=True)
class Position:
    x: float
    y: float

    def __post_init__(self):
        # Check if coordinates are numeric
        if not isinstance(self.x, (int, float)) or not isinstance(self.y, (int, float)):
            raise InvalidPositionError(
                f"Coordinates must be numeric, got x: {type(self.x).__name__}, y: {type(self.y).__name__}."
            )

    @lru_cache(maxsize=None)
    def distance_to(self, other: 'Position') -> float:
        """Calculate the distance to another Position."""
        if not isinstance(other, Position):
            raise ValueError("The argument must be a Position instance.")
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def move(self, angle: 'Degrees', steps: int) -> 'Position':
        """Move the position by a certain number of steps in the specified angle."""
        if not isinstance(angle, Degrees):
            raise ValueError("Angle must be a Degrees instance.")

        rad_angle = angle.to_radians()
        dx = steps * cos(rad_angle)
        dy = steps * sin(rad_angle)
        return Position(self.x + dx, self.y + dy)

    def is_in(self, top_left: 'Position', bottom_right: 'Position') -> bool:
        """Check if the position is within a defined rectangular area."""
        if not all(isinstance(p, Position) for p in [top_left, bottom_right]):
            raise ValueError("Top left and bottom right must be Position instances.")
        return (top_left.x <= self.x <= bottom_right.x and
                bottom_right.y <= self.y <= top_left.y)

    def __add__(self, other: 'Position') -> 'Position':
        """Add two positions."""
        if not isinstance(other, Position):
            raise ValueError("The argument must be a Position instance.")
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Position') -> 'Position':
        """Subtract two positions."""
        if not isinstance(other, Position):
            raise ValueError("The argument must be a Position instance.")
        return Position(self.x - other.x, self.y - other.y)

    def __eq__(self, other: object) -> bool:
        """Check equality of two positions."""
        if not isinstance(other, Position):
            return NotImplemented
        return isclose(self.x, other.x, abs_tol=1e-9) and isclose(self.y, other.y, abs_tol=1e-9)

    def __repr__(self):
        return f"Position(x={self.x}, y={self.y})"

    def __str__(self) -> str:
        return f"({self._format_value(self.x)}, {self._format_value(self.y)})"

    @staticmethod
    def _format_value(value: float) -> str:
        """Format value for string representation."""
        if abs(value - round(value)) < 1e-6:
            return f"{round(value)}"
        else:
            return f"{value:.6f}"
