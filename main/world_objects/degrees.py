from math import radians


class InvalidAngleError(Exception):
    """Custom exception for invalid angle input."""
    pass


class Degrees:
    _angle_cache = {}

    def __init__(self, angle: float):
        if not isinstance(angle, (int, float)):
            raise InvalidAngleError(f"Angle must be a number, got {type(angle).__name__}.")
        self._angle = self._normalize_angle(angle)

    @property
    def angle(self) -> float:
        return self._angle

    @angle.setter
    def angle(self, angle: float):
        if not isinstance(angle, (int, float)):
            raise InvalidAngleError(f"Angle must be a number, got {type(angle).__name__}.")
        self._angle = self._normalize_angle(angle)

    @staticmethod
    def _normalize_angle(angle: float) -> float:
        if angle in Degrees._angle_cache:
            return Degrees._angle_cache[angle]
        normalized = angle % 360
        Degrees._angle_cache[angle] = normalized
        return normalized

    def turn_left(self, degrees: float = 90) -> 'Degrees':
        return Degrees(self._normalize_angle(self.angle - degrees))

    def turn_right(self, degrees: float = 90) -> 'Degrees':
        return Degrees(self._normalize_angle(self.angle + degrees))

    def to_radians(self) -> float:
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
