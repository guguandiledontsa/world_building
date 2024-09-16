class Degrees:
    def __init__(self, angle:float):
        self._angle = self._normalize_angle(angle)

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, angle:float):
        self._angle = self._normalize_angle(angle)

    @staticmethod
    def _normalize_angle(angle) -> float:
        return angle % 360

    def turn_left(self, degrees: float = 90) -> 'Degrees':
        """Turn left by the given number of degrees and return a new Degrees instance."""
        new_angle = self._normalize_angle(self.angle - degrees)
        return Degrees(new_angle)

    def turn_right(self, degrees: float = 90) -> 'Degrees':
        """Turn right by the given number of degrees and return a new Degrees instance."""
        new_angle = self._normalize_angle(self.angle + degrees)
        return Degrees(new_angle)


    def __eq__(self, other):
        if not isinstance(other, Degrees):
            return NotImplemented
        return abs(self.angle - other.angle) < 1e-9

    def __hash__(self):
        return hash(round(self.angle, 9))  # Use rounded value for consistent hashing

    def __repr__(self):
        return f"Degrees(angle={self.angle})"

    def __str__(self):
        return f"{self.angle}°"
