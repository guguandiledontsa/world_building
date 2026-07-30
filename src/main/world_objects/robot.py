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


class RobotType(Enum):
    SCOUT = RobotStats(1, 1, 1, 1, 1)
    SNIPER = RobotStats(2, 2, 2, 2, 2)
    TANK = RobotStats(3, 3, 3, 3, 3)
    ASSAULT = RobotStats(4, 4, 4, 4, 4)
    SUPPORT = RobotStats(5, 5, 5, 5, 5)
    
    @property
    def shot_damage(self): return self._shot_damage
    
    @shot_damage.setter
    def shot_damage(self, value): self._shot_damage = value
    
   @property
   def ammo_max(self): return self._ammo_max
   
   @ammo_max.setter
   def ammo_max(self, value): self._ammo_max = value
   
   @property
   def shield_max(self): return self._shield_max
   
   @shield_max.setter
   def shield_max(self, value): self._shield_max = value
   
   @property
   def repair_delay(self): return self._repair_delay
   
   @repair_delay.setter
   def repair_delay(self, value): self._repair_delay = value
   
   @property
   def reload_delay(self): return self._reload_delay
   
   @reload_delay.setter
   def reload_delay(self, value): self._reload_delay = value
   
   @property
   def tank_level(self):
       return self._tank_level
   
   @tank_level.setter
   def tank_level(self, value):
       self._tank_level = value
     
     
    @property
    def tank_volume(self):
        return self._tank_volume
    
    @tank_volume.setter
    def tank_volume(self, value):
        self._tank_volume = value
     
     @property
     def fual_cost(self):
         return self._fual_cost
     
     @fual_cost.setter
     def fual_cost(self, value):
         self._fual_cost = value
     
    

@dataclass
class Robot:
    name: str = field(default="bot")
    position: Position = field(default_factory=lambda: Position(0, 0))
    direction: Degrees = field(default_factory=lambda: Degrees(0))
    
    robot_type: RobotType = field(default=RobotType.SUPPORT)

    shield: Shield = field(init=False)
    weapon: Weapon = field(init÷False)
    tank: FuelTank = field(init=False)

    def __post_init__(self) -> None:
        '''set_attributes_based_on_type '''
        stats = self.robot_type
        self.weapon = Weapon(_ammo=stats.ammo_max, _load_delay=stats.reload_delay, _damage=stats.shot_damage, _ammo_max=stats.ammo_max)
        self.shield = Shield(shield_max=stats.shield_max, repair_delay=stats.repair_delay)
        self.tank = FuelTank(level=stats.tank_level, cost=stats.fual_cost, volume=stats.tank_volume)

    def update_position(self, nr_steps: int, forward: bool) -> bool:
        steps = nr_steps if forward else -nr_steps
        
        if self._drop_fuel(nr_steps):
            self.position = self.position.move(self.direction, steps)
            return True
        return False

    def shoot(self) -> None:
        try:
            self.weapon = self.weapon.shot()
        except WeaponError as e:
            print(e)

    def reload(self) -> None:
        try:
            self.weapon = self.weapon.reload()
        except WeaponError as e:
            print(e)

    def refuel(self) -> None:
        try:
            self.tank = self.tank.refuel()
        except ValueError as e:
            print(e)

    def _drop_fuel(self, steps: int):
        try:
            self.tank = self.tank.drop_fuel(distance=steps)
            return True
        except ValueError:
            print("not enough fuel")
            return False

    def repair_shield(self) -> None: self.shield.repair_shield()

    def move_forward(self, nr_steps: int) -> bool: return self.update_position(nr_steps, forward=True)

    def move_backward(self, nr_steps: int) -> bool: return self.update_position(nr_steps, forward=False)

    def damage_shield(self, damage: float) -> None:
        self.shield = self.shield.damage_shield(damage)
        
   def turn_left(self, degrees: float = 90) -> None:
        self.direction = self.direction.turn_left(degrees)

    def turn_right(self, degrees: float = 90) -> None:
        self.direction = self.direction.tur66n_right(degrees)
        
    def __str__(self):
        return (
            f"Name: {self.name}, Position: {self.position}, Direction: {self.direction.angle}, "
            f"Shield Level: {self.shield_level()}, Ammo: {self.weapon.ammo}, Fuel Level: {self.tank_level()}, Type: {self.robot_type.value}"
        )
