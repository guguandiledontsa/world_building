from dataclasses import dataclass, field
from math import radians, isclose
from functools import lru_cache

class InvalidAngleError(Exception):
    """Custom exception for invalid angle values."""
    pass

@dataclass(frozen=True)
class Degrees:
    _angle: float = field(init=True, repr=False)

    def __post_init__(self):
        # Normalize the angle using the setter
        object.__setattr__(self, '_angle', self._normalize_angle(self._angle))

    @property
    def angle(self) -> float:
        """Get the normalized angle."""
        return self._angle

    @staticmethod
    @lru_cache(maxsize=None)
    def _normalize_angle(angle: float) -> float:
        """Normalize the angle to be within [0, 360) degrees."""
        return angle % 360

    def turn_left(self, degrees: float = 90) -> 'Degrees':
        """Turn left by the given number of degrees."""
        return Degrees(self._normalize_angle(self.angle - degrees))

    def turn_right(self, degrees: float = 90) -> 'Degrees':
        """Turn right by the given number of degrees."""
        return Degrees(self._normalize_angle(self.angle + degrees))

    def to_radians(self) -> float:
        """Convert degrees to radians."""
        return radians(self.angle)

    def __add__(self, other: 'Degrees') -> 'Degrees':
        """Add two Degrees instances."""
        if not isinstance(other, Degrees): # type: ignore
            raise ValueError("The argument must be a Degrees instance.")
        return Degrees(self._normalize_angle(self.angle + other.angle))

    def __sub__(self, other: 'Degrees') -> 'Degrees':
        """Subtract two Degrees instances."""
        if not isinstance(other, Degrees): # type: ignore
            raise ValueError("The argument must be a Degrees instance.")
        return Degrees(self._normalize_angle(self.angle - other.angle))

    def __eq__(self, other: object) -> bool:
        """Check equality of two Degrees instances."""
        if not isinstance(other, Degrees):
            return NotImplemented
        return isclose(self.angle, other.angle, abs_tol=1e-9)

    def __hash__(self) -> int:
        """Return a hash of the angle for hashable collections."""
        return hash(round(self.angle, 9))

    def __repr__(self) -> str:
        return f"Degrees(angle={self.angle})"

    def __str__(self) -> str:
        return f"{self.angle}°"
