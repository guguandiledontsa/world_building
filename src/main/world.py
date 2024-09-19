from dataclasses import dataclass, field
from typing import Dict, List
from main.world_objects.position import Position
from main.world_objects.degrees import Degrees
from main.world_objects.robot import Robot


@dataclass
class World:
    robots: Dict[str, Robot] = field(default_factory=dict)

    def spawn_robot(self, name: str, position: Position, direction: Degrees, type: str = "basic") -> None:
        """Spawn a new robot with the given name, position, direction, and type."""
        if name in self.robots:
            raise ValueError(f"A robot with the name '{name}' already exists.")
        self.robots[name] = Robot(name=name, position=position, current_direction=direction, type=type)

    def get_robot(self, name: str) -> Robot:
        """Get a robot by name."""
        return self.robots.get(name)

    def move_robot(self, name: str, nr_steps: int, forward: bool) -> bool:
        """Move a robot by a certain number of steps."""
        robot = self.get_robot(name)
        if robot:
            return robot.update_position(nr_steps, forward)
        return False

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

    def __str__(self):
        return f"World with robots: {', '.join(self.list_robots())}"


if __name__ == "__main__":
    # Initialize the world
    # world = World()
    # print(world)
    #
    # # Spawn some robots
    # world.spawn_robot(name="Robo1", position=Position(0, 0), direction=Degrees(0), type="scout")
    # print(world)
    # world.spawn_robot(name="Robo2", position=Position(5, 5), direction=Degrees(90), type="sniper")
    # print(world)
    #
    # # Move robots
    # world.move_robot(name="Robo1", nr_steps=10, forward=True)  # Move Robo1 forward by 10 steps
    # world.turn_robot_left(name="Robo2", degrees=90)  # Turn Robo2 left by 90 degrees
    #
    # # List all robots
    # print(world.list_robots())  # Output: ['Robo1', 'Robo2']
    #
    # # Get robot details
    # robot = world.get_robot(name="Robo1")
    # print(robot)  # Output: Name: Robo1
    #
    # robot = world.get_robot(name="Robo2")
    # print(robot)  # Output: Name: Robo1
    pass
