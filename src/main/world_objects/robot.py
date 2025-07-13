from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from src.main.world_objects.robot_objects.fuel_tank import FuelTank
from src.main.world_objects.robot_objects.position import Position
from src.main.world_objects.robot_objects.degrees import Degrees
from src.main.world_objects.robot_objects.shield import Shield
from src.main.world_objects.robot_objects.weapon import Weapon, WeaponError


class RobotType(Enum):
    SCOUT = "scout"
    SNIPER = "sniper"
    TANK = "tank"
    ASSAULT = "assault"
    SUPPORT = "support"


@dataclass
class Robot:
    name: str
    position: Position = field(default_factory=lambda: Position(0, 0))
    direction: Degrees = field(default_factory=lambda: Degrees(0))
    shield: Shield = field(default_factory=lambda: Shield(shield_max=5))
    weapon: Weapon = field(default_factory=lambda: Weapon(_ammo=5))
    tank: FuelTank = field(default_factory=lambda: FuelTank(volume=50))
    type: str = field(default=RobotType.SUPPORT)

    def __post_init__(self):
        self.set_attributes_based_on_type()

    def set_attributes_based_on_type(self):
        # Define attributes based on the RobotType Enum
        type_attributes = {
            RobotType.SCOUT: (1, 5, 1, 2, 2),
            RobotType.SNIPER: (5, 1, 1, 4, 5),
            RobotType.TANK: (3, 5, 5, 5, 3),
            RobotType.ASSAULT: (2, 3, 3, 3, 3),
            RobotType.SUPPORT: (1, 4, 2, 3, 2),
        }

        # Look up attributes based on the robot's type
        attributes = type_attributes.get(self.type)
        if attributes:
            shot_damage, ammo_max, shield_max, repair_delay, reload_delay = attributes
            self.weapon = Weapon(
                _ammo=ammo_max, _load_delay=reload_delay, _damage=shot_damage, _ammo_max=ammo_max)
            self.shield = Shield(shield_max=shield_max,
                                 repair_delay=repair_delay)

    def update_position(self, nr_steps: int, forward: bool) -> bool:
        steps = nr_steps if forward else -nr_steps
        
        if self._drop_fuel(nr_steps):
            self.position = self.position.move(self.direction, steps)
            return True
        return False

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
            print(f"{e}")

    def reload(self) -> None:
        try:
            self.weapon = self.weapon.reload()
        except WeaponError as e:
            print(e)

    def shield_level(self) -> Optional[int]:
        return self.shield.level

    def tank_level(self) -> float:
        return self.tank.level

    def refuel(self) -> None:
        try:
            self.tank = self.tank.refuel()
        except ValueError as e:
            print(e)

    def _drop_fuel(self, steps: int):
        try:
            self.tank = self.tank.drop_fuel(
                distance=steps)
            return True
        except ValueError:
            print(
                "not enough fuel")
            return False

    def __str__(self):
        return (
            f"Name: {self.name}, Position: {self.position}, Direction: {self.direction.angle}, "
            f"Shield Level: {self.shield_level()}, Ammo: {self.weapon.ammo}, Fuel Level: {self.tank_level()}, Type: {self.type}"
        )
