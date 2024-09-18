from math import radians

class InvalidAngleError(ValueError):
    """Exception raised for invalid angle values."""
    pass

class Degrees:
    def __init__(self, angle: float):
        """Initialize a Degrees instance with a normalized angle."""
        if not isinstance(angle, (int, float)):
            raise InvalidAngleError(f"Angle must be a number, got {type(angle).__name__}.")
        self._angle = self._normalize_angle(angle)

    @property
    def angle(self) -> float:
        """Get the current angle in degrees."""
        return self._angle

    @angle.setter
    def angle(self, angle: float):
        """Set the angle, normalizing it."""
        if not isinstance(angle, (int, float)):
            raise InvalidAngleError(f"Angle must be a number, got {type(angle).__name__}.")
        self._angle = self._normalize_angle(angle)

    @staticmethod
    def _normalize_angle(angle: float) -> float:
        """Normalize the angle to be within 0 to 360 degrees."""
        return angle % 360

    def turn_left(self, degrees: float = 90) -> 'Degrees':
        """Turn left by the given number of degrees and return a new Degrees instance."""
        return Degrees(self._normalize_angle(self.angle - degrees))

    def turn_right(self, degrees: float = 90) -> 'Degrees':
        """Turn right by the given number of degrees and return a new Degrees instance."""
        return Degrees(self._normalize_angle(self.angle + degrees))

    def to_radians(self) -> float:
        """Convert degrees to radians."""
        return radians(self.angle)

    def __eq__(self, other) -> bool:
        """Check equality with another Degrees instance."""
        if not isinstance(other, Degrees):
            return NotImplemented
        return abs(self.angle - other.angle) < 1e-9

    def __hash__(self) -> int:
        """Return a hash based on the angle."""
        return hash(round(self.angle, 9))

    def __repr__(self) -> str:
        """Return a string representation of the Degrees instance."""
        return f"Degrees(angle={self.angle})"

    def __str__(self) -> str:
        """Return the angle as a string with the degree symbol."""
        return f"{self.angle}°"
