from math import radians, isclose
from functools import lru_cache

class Degrees:
    def __init__(self, angle: float):
        self._angle = self._normalize_angle(angle)

    @property
    def angle(self) -> float:
        return self._angle

    @angle.setter
    def angle(self, angle: float):
        self._angle = self._normalize_angle(angle)

    @staticmethod
    @lru_cache(maxsize=None)
    def _normalize_angle(angle: float) -> float:
        """Normalize the angle to be within [0, 360)."""
        return angle % 360

    def turn_left(self, degrees: float = 90) -> 'Degrees':
        return Degrees(self._normalize_angle(self.angle - degrees))

    def turn_right(self, degrees: float = 90) -> 'Degrees':
        return Degrees(self._normalize_angle(self.angle + degrees))

    def to_radians(self) -> float:
        return radians(self.angle)

    def __eq__(self, other):
        if not isinstance(other, Degrees):
            return NotImplemented
        return isclose(self.angle, other.angle, abs_tol=1e-9)

    def __hash__(self):
        return hash(round(self.angle, 9))

    def __repr__(self) -> str:
        return f"Degrees(angle={self.angle})"

    def __str__(self) -> str:
        return f"{self.angle}°"
