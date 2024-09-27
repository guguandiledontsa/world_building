import unittest
from math import radians, cos, sin, isclose

from src.main.world_objects.robot_objects.position import Position
from src.main.world_objects.robot_objects.degrees import Degrees


class TestPosition(unittest.TestCase):

    def setUp(self):
        self.start_pos = Position(0, 0)

    def test_initial_position(self):
        pos = Position(0, 0)
        self.assertEqual(pos.x, 0)
        self.assertEqual(pos.y, 0)

    def test_move_north(self):
        angle = Degrees(90)
        new_pos = self.start_pos.move(angle, 10)
        self.assertTrue(isclose(new_pos.x, 0, abs_tol=1e-9))
        self.assertTrue(isclose(new_pos.y, 10, abs_tol=1e-9))

    def test_move_south(self):
        angle = Degrees(270)
        new_pos = self.start_pos.move(angle, 10)
        self.assertTrue(isclose(new_pos.x, 0, abs_tol=1e-9))
        self.assertTrue(isclose(new_pos.y, -10, abs_tol=1e-9))

    def test_move_east(self):
        angle = Degrees(0)
        new_pos = self.start_pos.move(angle, 10)
        self.assertTrue(isclose(new_pos.x, 10, abs_tol=1e-9))
        self.assertTrue(isclose(new_pos.y, 0, abs_tol=1e-9))

    def test_move_west(self):
        angle = Degrees(180)
        new_pos = self.start_pos.move(angle, 10)
        self.assertTrue(isclose(new_pos.x, -10, abs_tol=1e-9))
        self.assertTrue(isclose(new_pos.y, 0, abs_tol=1e-9))

    def test_move_multiple_directions(self):
        pos = Position(1, 1)
        new_pos = pos.move(Degrees(90), 3).move(Degrees(0), 2)
        self.assertTrue(isclose(new_pos.x, 3, abs_tol=1e-9))
        self.assertTrue(isclose(new_pos.y, 4, abs_tol=1e-9))

    def test_move_zero_steps(self):
        pos = Position(5, -5)
        new_pos = pos.move(Degrees(90), 0)
        self.assertEqual(new_pos, pos)

    def test_move_large_steps(self):
        pos = Position(0, 0)
        new_pos = pos.move(Degrees(90), 1000000)
        self.assertTrue(isclose(new_pos.x, 0, abs_tol=1e-9))
        self.assertTrue(isclose(new_pos.y, 1000000, abs_tol=1e-9))

    def test_move_negative_steps(self):
        pos = Position(10, 10)
        new_pos = pos.move(Degrees(180), -5)
        self.assertTrue(isclose(new_pos.x, 15, abs_tol=1e-9))
        self.assertTrue(isclose(new_pos.y, 10, abs_tol=1e-9))

    def test_move_without_direction(self):
        # Move North (90 degrees) by 2 steps
        pos_after_north = self.start_pos.move(Degrees(90), 2)
        print(f"After moving North: {pos_after_north}")
        self.assertTrue(isclose(pos_after_north.x, 0, abs_tol=1e-6))
        self.assertTrue(isclose(pos_after_north.y, 2, abs_tol=1e-6))

        # Move West (180 degrees) by 1 step from the new position
        pos_after_west = pos_after_north.move(Degrees(180), 1)
        print(f"After moving West: {pos_after_west}")
        self.assertTrue(isclose(pos_after_west.x, -1, abs_tol=1e-6))
        self.assertTrue(isclose(pos_after_west.y, 2, abs_tol=1e-6))

        # Move South (270 degrees) by 2 steps from the new position
        pos_after_south = pos_after_west.move(Degrees(270), 2)
        print(f"After moving South: {pos_after_south}")
        self.assertTrue(isclose(pos_after_south.x, -1, abs_tol=1e-6))
        self.assertTrue(isclose(pos_after_south.y, 0, abs_tol=1e-6))

        # Move East (0 degrees) by 1 step from the new position
        pos_after_east = pos_after_south.move(Degrees(0), 1)
        print(f"After moving East: {pos_after_east}")
        self.assertTrue(isclose(pos_after_east.x, 0, abs_tol=1e-6))
        self.assertTrue(isclose(pos_after_east.y, 0, abs_tol=1e-6))
        #
        # # Check that the final position is the same as the starting position
        self.assertEqual(pos_after_east, self.start_pos)

    def test_angle_normalization(self):
        angle = Degrees(450)  # Equivalent to 90 degrees
        new_pos = self.start_pos.move(angle, 10)
        self.assertTrue(isclose(new_pos.x, 0, abs_tol=1e-9))
        self.assertTrue(isclose(new_pos.y, 10, abs_tol=1e-9))

    def test_negative_angle(self):
        angle = Degrees(-45)  # Equivalent to 315 degrees
        steps = 10
        rad_angle = radians(angle.angle)
        expected_x = steps * cos(radians(45))
        expected_y = -steps * sin(radians(45))
        new_pos = self.start_pos.move(angle, steps)
        self.assertTrue(isclose(new_pos.x, expected_x, abs_tol=1e-9))
        self.assertTrue(isclose(new_pos.y, expected_y, abs_tol=1e-9))


if __name__ == "__main__":
    unittest.main()
