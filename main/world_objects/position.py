from .degrees import Degrees
from math import isclose

from dataclasses import dataclass, field
from typing import Tuple, Callable, Dict
from math import sqrt, cos, sin, radians


@dataclass(frozen=True)
class Position:
    x: float
    y: float

    def move(self, angle:'Degrees', steps:int) -> 'Position':
        rad_angle = radians(angle.angle)
        dx = steps * cos(rad_angle)
        dy = steps * sin(rad_angle)
        return Position(self.x + dx, self.y + dy)

    def distance_to(self, other:'Position') -> float:
        """Calculate the distance to another Position."""
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2) # type: ignore

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
        # Format x and y values with up to 6 decimal places if needed
        return f"({self._format_value(self.x)}, {self._format_value(self.y)})"

    @staticmethod
    def _format_value(value: float) -> str:
        if abs(value - round(value)) < 1e-6:
            # If the value is close to an integer, format without decimals
            return f"{round(value)}"
        else:
            # Otherwise, format with up to 6 decimal places
            return f"{value:.6f}"
    
if __name__ == "__main__":
    ...
