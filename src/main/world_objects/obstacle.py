import random
from dataclasses import dataclass, asdict
from typing import List

from src.main.world_objects.robot_objects.position import Position


def gen_fence(fence: List[Position], length: int, max_attempts: int = 10) -> List[Position]:
    head = fence[-1]  # Current head position of the fence
    tried_positions = set()  # Set to track tried positions
    attempts = 0  # Track the number of attempts

    while len(fence) < length:
        possible_next = random.choice(head.surrounding())

        # Debug: Print the possible next position
        # print(f"Trying position: {possible_next}")

        # Check if this position is already part of the fence or has been tried
        if possible_next not in [(p.x, p.y) for p in fence] and possible_next not in tried_positions:
            fence.append(Position(possible_next[0], possible_next[1]))  # Add to fence
            # print(f"Added position: {possible_next}")  # Debug: Print added position
            tried_positions.clear()  # Clear tried positions since we found a valid next
            return gen_fence(fence, length, max_attempts)  # Recur to continue building

        # Mark this position as tried
        tried_positions.add(possible_next)
        attempts += 1

        # If maximum attempts reached, break out of the loop
        if attempts >= max_attempts:
            print("No valid next position found, stopping.")
            return fence

    return fence


def visualize_fence(fence: List[Position], grid_size: int = 5):
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

    for position in fence:
        if 0 <= position.x < grid_size and 0 <= position.y < grid_size:
            grid[position.y][position.x] = '#'

    for row in grid:
        print(" ".join(row))



class Obstacle:

    def __init__(self, position: 'Position'):
        self.position = position
        self.fence = gen_fence([self.position], 5)

    @property
    def position(self) -> Position:
        return self._position
    @position.setter
    def position(self, value):
        self._position = value

    @property
    def fence(self) -> List[Position]:
        return self._fence
    @fence.setter
    def fence(self, value: List[Position]):
        self._fence = value


if __name__ == "__main__":
    # Usage
    starting_position = Position(2, 2)
    fence = [starting_position]
    length = 50  # Length of the fence you want to generate

    fence = gen_fence(fence, length)
    visualize_fence(fence, 10)
