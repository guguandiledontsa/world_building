from dataclasses import dataclass, field
from typing import Dict, List

from src.main.world_objects.robot_objects.fuel_tank import FuelTank
from src.main.world_objects.robot_objects.position import Position
from src.main.world_objects.robot_objects.degrees import Degrees
from src.main.world_objects.robot import Robot
from src.main.world_objects.robot_objects.weapon import Weapon


@dataclass
class World:
    robots: Dict[str, Robot] = field(default_factory=dict)

    def spawn_robot(
        self, name: str, position: Position, direction: Degrees, robot_type: str = "basic", tank: 'FuelTank'= FuelTank()
    ) -> Robot:
        """Spawn a new robot with the given name, position, direction, and type."""
        name = name.lower()
        if name in self.robots:
            raise ValueError(f"A robot with the name '{name}' already exists.")
        self.robots[name] = Robot(
            name=name, position=position, direction=direction,robot_type=robot_type, tank=tank
        )
        return self.robots[name]

    def get_robot(self, name: str) -> Robot:
        """Get a robot by name."""
        name = name.lower()
        return self.robots.get(name)  #

    def move_robot(self, name: str, steps: int, forward: bool) -> bool:
        """Move a robot by a certain number of steps."""
        robot = self.get_robot(name)
        if robot:
            return robot.update_position(steps, forward)
        return False

    def move_robot_forward(self, name: str, steps: int = 0):
        return self.move_robot(name=name, steps=steps, forward=True)
    def move_robot_back(self, name: str, steps: int = 0):
        return self.move_robot(name=name, steps=steps, forward=False)

    def turn_robot_left(self, name: str, degrees: float = 90) -> None:
        """Turn a robot left by a certain number of degrees."""
        robot = self.get_robot(name)
        if robot:
            robot.turn_left(degrees)
    def turn_robot_right(self, name: str, degrees: float = 90) -> None:
        """Turn a robot right by a certain number of degrees."""
        robot = self.get_robot(name)
        if robot:
            robot.turn_right(degrees)

    def list_robots(self) -> List[str]:
        """List all robot names in the world."""
        return list(self.robots.keys())

    def shoot(self, shooter_name: str) -> None:
        shooter = self.get_robot(shooter_name)
        if not shooter or shooter.weapon.ammo <= 0:
            print(f"{shooter_name} cannot shoot: Out of ammo.")
            return

        # Update ammo and set status
        gun = shooter.weapon
        shooter.weapon = Weapon(gun.ammo_max,gun.ammo-1, gun.damage, gun.loading, gun.load_delay)
        # shooter.set_status(f"{shooter.name} fired weapon.")

        shooter_x, shooter_y = shooter.position.x, shooter.position.y
        shot_direction = shooter.direction
        # targets_hit = []

        for bot in self.robots.values():
            if bot.name == shooter_name:
                continue

            bot_x, bot_y = bot.position.x, bot.position.y

            # Check if bot is in the line of fire
            is_in_line_of_fire = (
                    (bot_y == shooter_y and
                     ((bot_x < shooter_x and shot_direction == Degrees(180)) or
                      (bot_x > shooter_x and shot_direction == Degrees(0)))) or
                    (bot_x == shooter_x and
                     ((bot_y < shooter_y and shot_direction == Degrees(270)) or
                      (bot_y > shooter_y and shot_direction == Degrees(90))))
            )

            if is_in_line_of_fire:
                bot.damage_shield(gun.damage)  # Apply damage, adjust as needed
                # targets_hit.append(bot.name)
                # bot.set_status(f"{bot.name} was shot.")
                return


    def __str__(self):
        return f"World with robots: {', '.join(self.list_robots())}"
