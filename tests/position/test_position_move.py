import unittest
from main.direction import Direction
from main.position import Position

class MyTestCase(unittest.TestCase):
    def test_initial_position(self):
        pos = Position(0, 0)
        self.assertEqual(pos.x, 0)
        self.assertEqual(pos.y, 0)

    def test_move_north(self):
        pos = Position(0, 0)
        new_pos = pos.move(Direction.NORTH, 5)
        self.assertEqual(new_pos, Position(0, 5))

    def test_move_south(self):
        pos = Position(0, 0)
        new_pos = pos.move(Direction.SOUTH, 3)
        self.assertEqual(new_pos, Position(0, -3))

    def test_move_east(self):
        pos = Position(0, 0)
        new_pos = pos.move(Direction.EAST, 4)
        self.assertEqual(new_pos, Position(4, 0))

    def test_move_west(self):
        pos = Position(0, 0)
        new_pos = pos.move(Direction.WEST, 2)
        self.assertEqual(new_pos, Position(-2, 0))

    def test_move_multiple_directions(self):
        pos = Position(1, 1)
        new_pos = pos.move(Direction.NORTH, 3).move(Direction.EAST, 2)
        self.assertEqual(new_pos, Position(3, 4))

    def test_move_zero_steps(self):
        pos = Position(5, -5)
        new_pos = pos.move(Direction.NORTH, 0)
        self.assertEqual(new_pos, pos)

    def test_move_invalid_direction(self):
        pos = Position(1, 1)
        new_pos = pos.move(None, 5)  # Assuming we handle None as invalid direction
        self.assertEqual(new_pos, pos)

    def test_move_large_steps(self):
        pos = Position(0, 0)
        new_pos = pos.move(Direction.NORTH, 1000000)
        self.assertEqual(new_pos, Position(0, 1000000))

    def test_move_negative_steps(self):
        pos = Position(10, 10)
        new_pos = pos.move(Direction.WEST, -5)
        self.assertEqual(new_pos, Position(15, 10))

    def test_move_without_direction(self):
        pos = Position(1, 1)
        new_pos = pos.move(Direction.NORTH, 2).move(Direction.WEST, 1).move(Direction.SOUTH, 2).move(Direction.EAST, 1)
        self.assertEqual(new_pos, pos)


if __name__ == '__main__':
    unittest.main()
