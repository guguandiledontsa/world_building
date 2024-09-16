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