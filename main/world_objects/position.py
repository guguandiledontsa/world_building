from dataclasses import dataclass
from math import sqrt, cos, sin, radians, isclose

from main.world_objects.degrees import Degrees


class InvalidPositionError(ValueError):
    """Exception raised for invalid position values."""
    pass

@dataclass(frozen=True)
class Position:
    x: float
    y: float

    def __post_init__(self):
        """Validate the position coordinates."""
        if not isinstance(self.x, (int, float)) or not isinstance(self.y, (int, float)):
            raise InvalidPositionError(f"Coordinates must be numeric, got x: {type(self.x).__name__}, y: {type(self.y).__name__}.")

    def move(self, angle: 'Degrees', steps: int) -> 'Position':
        """Move the position in the direction specified by the angle by the given number of steps."""
        rad_angle = radians(angle.angle)
        dx = steps * cos(rad_angle)
        dy = steps * sin(rad_angle)
        return Position(self.x + dx, self.y + dy)

    def distance_to(self, other: 'Position') -> float:
        """Calculate the distance to another Position."""
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def is_in(self, top_left: 'Position', bottom_right: 'Position') -> bool:
        """Check if the position is within the bounding box defined by two corners."""
        return (top_left.x <= self.x <= bottom_right.x and
                bottom_right.y <= self.y <= top_left.y)

    def __eq__(self, other: object) -> bool:
        """Check equality with another Position instance."""
        if not isinstance(other, Position):
            return NotImplemented
        return isclose(self.x, other.x, abs_tol=1e-9) and isclose(self.y, other.y, abs_tol=1e-9)

    def __repr__(self) -> str:
        """Return a string representation of the Position instance."""
        return f"Position(x={self.x}, y={self.y})"

    def __str__(self) -> str:
        """Return the position as a formatted string."""
        return f"({self._format_value(self.x)}, {self._format_value(self.y)})"

    @staticmethod
    def _format_value(value: float) -> str:
        """Format the value to display without decimals if it's close to an integer."""
        if abs(value - round(value)) < 1e-6:
            return f"{round(value)}"
        return f"{value:.6f}"
