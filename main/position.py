from .direction import Direction


from dataclasses import dataclass, field
from typing import Tuple, Callable, Dict

@dataclass(frozen=True)
class Position:
    x: float
    y: float

    # Dictionary mapping directions to movement functions
    direction_movers: Dict[Direction, Callable[[int], Tuple[float, float]]] = field(default_factory=lambda: {
        Direction.NORTH: (0, 1),
        Direction.SOUTH: (0, -1),
        Direction.EAST: (1, 0),
        Direction.WEST: (-1, 0)
    })

    def move(self, direction: Direction, steps: int) -> 'Position':
        mover = self.direction_movers.get(direction)
        if mover:
            dx, dy = mover
            new_position = Position(self.x + dx*steps, self.y + dy*steps)
            return new_position
        return self

    def distance_to(self, other:'Position') -> float:
        """Calculate the distance to another Position."""
        from math import sqrt # type: ignore
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2) # type: ignore

    def is_in(self, top_left: 'Position', bottom_right: 'Position') -> bool:
        return (top_left.x <= self.x <= bottom_right.x and
                bottom_right.y <= self.y <= top_left.y)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Position):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Position(x={self.x}, y={self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    
if __name__ == "__main__":
    ... 
