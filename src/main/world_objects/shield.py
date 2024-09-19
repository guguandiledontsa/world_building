from dataclasses import dataclass, field
import threading
from functools import lru_cache

@dataclass
class Shield:
    shield_max: int
    repair_delay: int = field(default=5)
    shield_level: int = field(init=False)
    is_repairing: bool = field(init=False, default=False)

    def __post_init__(self):
        self.shield_level = self.shield_max  # Start with max shield level

    @lru_cache(maxsize=None)  # Cache the shield level retrieval
    def get_shield_level(self) -> int:
        """Return the current shield level."""
        return self.shield_level

    def set_shield_level(self, new_shield_level: int) -> None:
        """Set the shield level and reset repairing status."""
        self.shield_level = max(new_shield_level, 0)
        self.is_repairing = False
        self.get_shield_level.cache_clear()  # Clear the cache when setting a new level

    def repair_shield(self) -> None:
        """Initiate a repair of the shield after a delay."""
        if self.shield_level < self.shield_max and not self.is_repairing:
            self.is_repairing = True
            threading.Timer(self.repair_delay, self.set_shield_level, [self.shield_max]).start()

    def damage_shield(self, damage: int) -> None:
        """Apply damage to the shield, reducing its level."""
        if self.shield_level > 0:
            self.shield_level -= damage
            self.get_shield_level.cache_clear()  # Clear the cache after damage

    def is_being_repaired(self) -> bool:
        """Check if the shield is currently being repaired."""
        return self.is_repairing

    def __eq__(self, other: 'Shield') -> bool: # type: ignore
        """Check if two shields are equal based on their levels and max values."""
        if not isinstance(other, Shield): # type: ignore
            return NotImplemented
        return (self.shield_level == other.shield_level and 
                self.shield_max == other.shield_max)

    def __lt__(self, other: 'Shield') -> bool:
        """Compare shields based on their shield levels."""
        if not isinstance(other, Shield): # type: ignore
            return NotImplemented
        return self.shield_level < other.shield_level

    def __add__(self, other: 'Shield') -> 'Shield':
        """Combine two shields and return a new shield."""
        if not isinstance(other, Shield): # type: ignore
            return NotImplemented
        combined_shield_level = min(self.get_shield_level() + other.get_shield_level(), self.shield_max) # type: ignore
        # Return a new Shield instance without the shield_level argument
        return Shield(shield_max=self.shield_max, repair_delay=self.repair_delay, )

    def __str__(self):
        return (f"Shield Level: {self.get_shield_level()}/{self.shield_max}, "
                f"Repairing: {self.is_repairing}")
