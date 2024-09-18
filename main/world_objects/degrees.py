from math import radians
from functools import lru_cache
from dataclasses import dataclass

class InvalidAngleError(Exception):
    """Custom exception for invalid angle values."""
    pass

@dataclass(frozen=True)
class Degrees:
    _angle: float

    def __post_init__(self):
        # Use the setter for normalization
        object.__setattr__(self, 'angle', self._angle)  # Uses the setter to normalize

    @property
    def angle(self) -> float:
        return self._angle

    @angle.setter
    def angle(self, value: float):
        if not isinstance(value, (int, float)):
            raise InvalidAngleError(f"Angle must be numeric, got {type(value).__name__}.")
        normalized = self._normalize_angle(value)
        object.__setattr__(self, '_angle', normalized)

    @staticmethod
    @lru_cache(maxsize=None)
    def _normalize_angle(angle: float) -> float:
        """Normalize the angle to be within the range [0, 360)."""
        return angle % 360

    def turn_left(self, degrees: float = 90) -> 'Degrees':
        """Turn left by the given number of degrees and return a new Degrees instance."""
        new_angle = self._normalize_angle(self.angle - degrees)
        return Degrees(new_angle)

    def turn_right(self, degrees: float = 90) -> 'Degrees':
        """Turn right by the given number of degrees and return a new Degrees instance."""
        new_angle = self._normalize_angle(self.angle + degrees)
        return Degrees(new_angle)

    def to_radians(self) -> float:
        """Convert degrees to radians."""
        return radians(self.angle)

    def __eq__(self, other):
        if not isinstance(other, Degrees):
            return NotImplemented
        return abs(self.angle - other.angle) < 1e-9

    def __hash__(self):
        return hash(round(self.angle, 9))

    def __repr__(self):
        return f"Degrees(angle={self.angle})"

    def __str__(self):
        return f"{self.angle}°"

    def __add__(self, other: 'Degrees') -> 'Degrees':
        """Add two Degrees instances."""
        if not isinstance(other, Degrees):
            return NotImplemented
        return Degrees(self._normalize_angle(self.angle + other.angle))

    def __sub__(self, other: 'Degrees') -> 'Degrees':
        """Subtract two Degrees instances."""
        if not isinstance(other, Degrees):
            return NotImplemented
        return Degrees(self._normalize_angle(self.angle - other.angle))
