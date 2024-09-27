from dataclasses import dataclass, field
from typing import Optional
from src.main.world_objects.position import Position
from src.main.world_objects.degrees import Degrees
from src.main.world_objects.shield import Shield
from src.main.world_objects.weapon import Weapon, WeaponError

@dataclass
class Robot:
    name: str
    position: Position = field(default_factory=lambda: Position(0, 0))
    direction: Degrees = field(default_factory=lambda: Degrees(0))
    shield: Shield = field(default_factory=lambda: Shield(shield_max=5))
    weapon: Weapon = field(default_factory=lambda: Weapon(_ammo=5))
    type: str = field(default="basic")

    def __post_init__(self):
        self.set_attributes_based_on_type()

    def set_attributes_based_on_type(self):
        type_attributes = {
            "scout": (1, 5, 1, 2, 2),
            "sniper": (5, 1, 1, 4, 5),
            "tank": (3, 5, 5, 5, 3),
            "assault": (2, 3, 3, 3, 3),
            "support": (1, 4, 2, 3, 2),
        }
        if self.type in type_attributes:
            (
                shot_damage,
                ammo_max,
                shield_max,
                repair_delay,
                reload_delay,
            ) = type_attributes[self.type]
            self.weapon = Weapon(_ammo=ammo_max,_load_delay=reload_delay, _damage=shot_damage, _ammo_max=ammo_max)
            self.shield = Shield(shield_max=shield_max, repair_delay=repair_delay)

    def update_position(self, nr_steps: int, forward: bool) -> bool:
        steps = nr_steps if forward else -nr_steps
        
        # fuel
        
        self.position = self.position.move(self.direction, steps)
        return True

    def move_forward(self, nr_steps: int) -> bool:
        return self.update_position(nr_steps, forward=True)

    def move_backward(self, nr_steps: int) -> bool:
        return self.update_position(nr_steps, forward=False)

    def turn_left(self, degrees: float = 90) -> None:
        self.direction = self.direction.turn_left(degrees)

    def turn_right(self, degrees: float = 90) -> None:
        self.direction = self.direction.turn_right(degrees)

    def damage_shield(self, damage: float) -> None:
        self.shield = self.shield.damage_shield(damage)

    def repair_shield(self) -> None:
        self.shield.repair_shield()

    def shoot(self) -> None:
        try:
            self.weapon = self.weapon.shot()
        except WeaponError as e:
            print(f"Weapon Error: {e}")



    def reload(self) -> None:
        try:
            self.weapon = self.weapon.reload()
        except WeaponError as e:
            print(e)

    def get_shield_level(self) -> Optional[int]:
        return self.shield.level

    def __str__(self):
        return (
            f"Name: {self.name}, Position: {self.position}, Direction: {self.direction.angle}, "
            f"Shield Level: {self.get_shield_level()}, Ammo: {self.weapon.ammo}, Type: {self.type}"
        )
