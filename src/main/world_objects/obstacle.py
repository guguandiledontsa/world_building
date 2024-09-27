from dataclasses import dataclass

from src.main.world_objects.robot_objects.position import Position


@dataclass
class Obstacle:
    position: Position
    width: float
    height: float


class Square(Obstacle):
    def __init__(self, position: Position, length: float):
        super().__init__(position, length, length)
