from dataclasses import dataclass, field
from typing import List

from main.world_objects.position import Position
from main.world_objects.degrees import Degrees  # Import Degrees instead of Direction

@dataclass
class Robot:
    name: str
    position: Position = field(default_factory=lambda: Position(0, 0))
    current_direction: Degrees = field(default_factory=lambda: Degrees(0))  # Use Degrees
    status: str = field(default="Ready")
    history: List[str] = field(default_factory=list)
    type: str = field(default="basic")  # Default type

    # Attributes with default values for non-specialized robots
    shot_damage: int = field(default=1)
    initial_ammo: int = field(default=5)
    shield_max: int = field(default=5)
    ammo: int = field(init=False)
    shield_level: int = field(init=False)
    repair_delay: int = field(default=5)
    reload_delay: int = field(default=5)
    is_reloading: bool = field(default=False)
    is_repairing: bool = field(default=False)

    def __post_init__(self):
        self.ammo = self.initial_ammo
        self.shield_level = self.shield_max
        self.set_attributes_based_on_type()

    def set_attributes_based_on_type(self):
        type_attributes = {
            "scout": (1, 5, 1, 2, 2),
            "sniper": (5, 1, 1, 4, 5),
            "tank": (3, 5, 5, 5, 3),
            "assault": (2, 3, 3, 3, 3),
            "support": (1, 4, 2, 3, 2)
        }
        if self.type in type_attributes:
            self.shot_damage, self.initial_ammo, self.shield_max, self.repair_delay, self.reload_delay = type_attributes[self.type]
            self.ammo = self.initial_ammo
            self.shield_level = self.shield_max

    def update_position(self, nr_steps: int, forward: bool) -> bool:
        steps = nr_steps if forward else -nr_steps
        new_position = self.position.move(self.current_direction, steps)
        self.position = new_position
        return True

    def move_forward(self, nr_steps: int) -> bool:
        """Move the robot forward by a given number of steps."""
        return self.update_position(nr_steps, forward=True)

    def move_backward(self, nr_steps: int) -> bool:
        """Move the robot backward by a given number of steps."""
        return self.update_position(nr_steps, forward=False)

    def turn_left(self, degrees: float = 90) -> None:
        """Turn the robot left by the given number of degrees."""
        self.current_direction = self.current_direction.turn_left(degrees)

    def turn_right(self, degrees: float = 90) -> None:
        """Turn the robot right by the given number of degrees."""
        self.current_direction = self.current_direction.turn_right(degrees)

    def __str__(self):
        return (f"Name: {self.name}, Position: {repr(self.position)}, Direction: {self.current_direction.angle}, "
                f"Status: {self.status}, Shield Level: {self.shield_level}, Ammo: {self.ammo}, Type: {self.type}")
