import threading
from dataclasses import dataclass, field

# Custom exception class
class WeaponError(Exception):
    """Base class for weapon-related exceptions."""
    def __init__(self, message: str):
        super().__init__(message)

@dataclass(frozen=True)
class Weapon:
    _ammo_max: int = field(default=5)
    _ammo: int = field(default=_ammo_max)
    _damage: float = field(default=1.0)
    _loading: bool = field(default=False)
    _load_delay: float = field(default=5.0)
    _lock: threading.Lock = field(default_factory=threading.Lock, init=False)

    def __post_init__(self):
        if self._ammo > self._ammo_max:
            raise ValueError("Ammo cannot exceed ammo_max")

    @property
    def ammo(self) -> int:
        return self._ammo

    # @ammo.setter
    # def ammo(self, value):
    #     # return Weapon(_ammo=value, _ammo_max=self._ammo_max, _damage=self._damage, _loading=self._loading, _load_delay=self._load_delay)
    #     self._ammo = value

    @property
    def ammo_max(self) -> int:
        return self._ammo_max

    @property
    def damage(self) -> float:
        return self._damage

    @property
    def loading(self) -> bool:
        return self._loading

    @property
    def load_delay(self) -> float:
        return self._load_delay

    @property
    def is_empty(self) -> bool:
        return self.ammo == 0

    @property
    def can_reload(self) -> bool:
        return not self._loading and self._ammo < self._ammo_max

    def shot(self) -> 'Weapon':
        if self.is_empty:
            raise WeaponError("Cannot shoot: Out of ammo, current ammo: {}".format(self.ammo))
        
        with self._lock:
            return Weapon(_ammo=self._ammo - 1, _ammo_max=self._ammo_max, _damage=self._damage,
                          _loading=self._loading, _load_delay=self._load_delay)

    def reload(self) -> 'Weapon':
        if self.loading:
            raise WeaponError("Already loading. Wait for the current reload to finish.")
        
        with self._lock:
            return Weapon(_ammo=self._ammo_max, _ammo_max=self._ammo_max, _damage=self._damage,
                          _loading=True, _load_delay=self._load_delay)

    def __hash__(self):
        return hash((self._ammo, self._ammo_max, self._damage, self._loading, self._load_delay))
