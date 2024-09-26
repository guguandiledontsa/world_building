from dataclasses import dataclass, field
import threading
from typing import Optional

@dataclass(frozen=True)
class Shield:
    level: Optional[int] = field(default=None)  # Input shield level
    shield_max: int = field(default=5)  # Default max shield level
    repair_delay: int = field(default=5)   # Default repair delay
    _is_repairing: bool = field(init=False, default=False)
    lock: threading.Lock = field(default_factory=threading.Lock, init=False)

    def __post_init__(self):
        # Normalize level to be >= 0 and <= shield_max
        if self.level is None:
            object.__setattr__(self, 'level', self.shield_max)
        else:
            normalized_level = min(max(self.level, 0), self.shield_max)
            object.__setattr__(self, 'level', normalized_level)

        object.__setattr__(self, '_is_repairing', False)  # Initialize repairing status

    @property
    def is_repairing(self) -> bool:
        """Check if the shield is currently being repaired."""
        with self.lock:
            return self._is_repairing

    def repair_shield(self) -> None:
        """Initiate a repair of the shield after a delay."""
        with self.lock:
            if self.level < self.shield_max and not self._is_repairing:
                object.__setattr__(self, '_is_repairing', True)
                threading.Timer(self.repair_delay, self._finish_repair).start()

    def _finish_repair(self) -> None:
        """Finish repairing the shield."""
        with self.lock:
            object.__setattr__(self, 'level', self.shield_max)
            object.__setattr__(self, '_is_repairing', False)

    def damage_shield(self, damage: int) -> 'Shield':
        """Apply damage to the shield, returning a new Shield instance with updated level."""
        with self.lock:
            new_level = max(self.level - damage, 0)
            return Shield(level=new_level, shield_max=self.shield_max, repair_delay=self.repair_delay)

    def __eq__(self, other: object) -> bool:
        """Check if two shields are equal based on their levels and max values."""
        if not isinstance(other, Shield):
            return NotImplemented
        return (self.level == other.level and 
                self.shield_max == other.shield_max)

    def __hash__(self) -> int:
        """Return the hash based on shield level and max."""
        return hash((self.level, self.shield_max))

    def __str__(self) -> str:
        return (f"Shield Level: {self.level}/{self.shield_max}, "
                f"Repairing: {self.is_repairing}")

    # def __lt__(self, other: 'object') -> bool:
    #     """Compare shields based on their shield levels."""
    #     if not isinstance(other, Shield):
    #         return NotImplemented
    #     return self.level < other.level
