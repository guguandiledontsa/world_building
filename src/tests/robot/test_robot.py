from unittest import mock
import unittest
from unittest.mock import patch

from src.main.world_objects.robot import Robot
from src.main.world_objects.position import Position
from src.main.world_objects.degrees import Degrees  # Updated import


class MyTestCase(unittest.TestCase):
    def setUp(self):
        # Setup default test robot
        self.default_robot = Robot(name="TestBot")

    def test_move_forward(self):
        """Test moving the robot forward."""
        self.default_robot.position = Position(0, 0)
        self.default_robot.direction = Degrees(90)  # Moving north

        self.default_robot.move_forward(5)
        self.assertEqual(self.default_robot.position, Position(0, 5))

    def test_move_backward(self):
        """Test moving the robot backward."""
        self.default_robot.position = Position(0, 0)
        self.default_robot.direction = Degrees(90)  # Moving north

        self.default_robot.move_backward(3)
        self.assertEqual(self.default_robot.position, Position(0, -3))

    def test_edge_cases(self):
        """Test edge cases for moving forward and backward."""
        self.default_robot.position = Position(0, 0)
        self.default_robot.direction = Degrees(0)  # Moving east

        # Moving forward
        self.default_robot.move_forward(10)
        self.assertEqual(self.default_robot.position, Position(10, 0))

        # Moving backward
        self.default_robot.move_backward(5)
        self.assertEqual(self.default_robot.position, Position(5, 0))

    def test_default_robot_initialization(self):
        robot = self.default_robot
        self.assertEqual(robot.name, "TestBot")
        self.assertEqual(robot.position, Position(0, 0))
        self.assertEqual(robot.direction, Degrees(0))  # Updated to Degrees
        # self.assertEqual(robot.status, "Ready")
        # self.assertEqual(robot.history, [])
        self.assertEqual(robot.type, "basic")
        self.assertEqual(robot.weapon.damage, 1)
        self.assertEqual(robot.weapon.ammo, 5)
        self.assertEqual(robot.shield.shield_max, 5)
        self.assertEqual(robot.weapon.ammo, 5)
        self.assertEqual(robot.shield.level, 5)
        self.assertEqual(robot.shield.repair_delay, 5)
        self.assertEqual(robot.weapon.load_delay, 5)
        self.assertFalse(robot.weapon.loading)
        self.assertFalse(robot.shield.is_repairing)

    def test_set_attributes_based_on_type(self):
        robot_types = {
            "scout": (1, 5, 1, 2, 2),
            "sniper": (5, 1, 1, 4, 5),
            "tank": (3, 5, 5, 5, 3),
            "assault": (2, 3, 3, 3, 3),
            "support": (1, 4, 2, 3, 2),
            "basic": (1, 5, 5, 5, 5)
        }

        for robot_type, attributes in robot_types.items():
            with self.subTest(robot_type=robot_type):
                robot = Robot(name="TestBot", type=robot_type)
                robot.set_attributes_based_on_type()
                self.assertEqual(robot.weapon.damage, attributes[0])
                self.assertEqual(robot.weapon.ammo_max, attributes[1])
                self.assertEqual(robot.shield.shield_max, attributes[2])
                self.assertEqual(robot.shield.repair_delay, attributes[3])
                self.assertEqual(robot.weapon.load_delay, attributes[4])
                self.assertEqual(robot.weapon.ammo, attributes[1])
                self.assertEqual(robot.shield.level, attributes[2])

    def test_update_position_forward(self):
        self.default_robot.position = Position(0, 0)
        self.default_robot.direction = Degrees(90)  # Updated to Degrees
        result = self.default_robot.update_position(3, forward=True)
        self.assertTrue(result)
        self.assertEqual(self.default_robot.position, Position(0, 3))

    def test_update_position_backward(self):
        self.default_robot.position = Position(0, 0)
        self.default_robot.direction = Degrees(90)  # Updated to Degrees
        result = self.default_robot.update_position(3, forward=False)
        self.assertTrue(result)
        self.assertEqual(self.default_robot.position, Position(0, -3))

    def test_str_method(self):
        robot = self.default_robot
        expected_str = (
            f"Name: TestBot, Position: (0, 0), Direction: {robot.direction.angle}, "
            f"Shield Level: 5, Ammo: 5, Type: basic"
        )
        self.assertEqual(str(robot), expected_str)

    def test_initial_ammo(self):
        robot = Robot(name="TestBot", type="sniper")
        self.assertEqual(robot.weapon.ammo, 1)

    def test_shield_max(self):
        robot = Robot(name="TestBot", type="tank")
        self.assertEqual(robot.shield.level, 5)

    def test_repair_and_reload_delays(self):
        robot = Robot(name="TestBot", type="support")
        self.assertEqual(robot.shield.repair_delay, 3)
        self.assertEqual(robot.weapon.load_delay, 2)

    def test_edge_case(self):
        robot = Robot(name="TestBot", type="unknown")
        robot.set_attributes_based_on_type()
        self.assertEqual(robot.weapon.damage, 1)  # Default values
        self.assertEqual(robot.weapon.ammo_max, 5)
        self.assertEqual(robot.shield.shield_max, 5)
        self.assertEqual(robot.shield.repair_delay, 5)
        self.assertEqual(robot.weapon.load_delay, 5)

    def test_turn_left(self):
        """Test turning left by 90 degrees."""
        self.default_robot.direction = Degrees(0)  # Facing East
        self.default_robot.turn_left()
        self.assertEqual(
            self.default_robot.direction.angle, 270
        )  # Should now be facing North

        self.default_robot.turn_left()  # Turn left again
        self.assertEqual(
            self.default_robot.direction.angle, 180
        )  # Should now be facing West

    def test_turn_right(self):
        """Test turning right by 90 degrees."""
        self.default_robot.direction = Degrees(0)  # Facing East
        self.default_robot.turn_right()
        self.assertEqual(
            self.default_robot.direction.angle, 90
        )  # Should now be facing South

        self.default_robot.turn_right()  # Turn right again
        self.assertEqual(
            self.default_robot.direction.angle, 180
        )  # Should now be facing West

    def test_turn_left_custom_degrees(self):
        """Test turning left by a custom number of degrees."""
        self.default_robot.direction = Degrees(180)  # Facing South
        self.default_robot.turn_left(45)
        self.assertEqual(
            self.default_robot.direction.angle, 135
        )  # Should now be facing Southeast

    def test_turn_right_custom_degrees(self):
        """Test turning right by a custom number of degrees."""
        self.default_robot.direction = Degrees(45)  # Facing Northeast
        self.default_robot.turn_right(45)
        self.assertEqual(
            self.default_robot.direction.angle, 90
        )  # Should now be facing East

    def test_update_position_with_mock(self):
        """Test move_forward and move_backward with mocked move method."""
        with mock.patch('src.main.world_objects.position.Position.move') as mock_move:
            mock_move.return_value = Position(10, 10)
            self.default_robot.position = Position(0, 0)
            direction = Degrees(45)  # Moving northeast
            self.default_robot.direction = direction

            # Testing move_forward
            self.default_robot.move_forward(15)
            mock_move.assert_called_with(direction, 15)
            self.assertEqual(self.default_robot.position, Position(10, 10))

            # Reset the mock and position
            mock_move.reset_mock()
            self.default_robot.position = Position(0, 0)

            # Testing move_backward
            self.default_robot.move_backward(10)
            mock_move.assert_called_with(direction, -10)
            self.assertEqual(self.default_robot.position, Position(10, 10))

    @patch('src.main.world_objects.position.Position.move')
    def test_update_position_with_mock1(self, mock_move):
        mock_move.return_value = Position(5, 5)
        self.default_robot.position = Position(0, 0)
        self.default_robot.direction = Degrees(45)  # Updated to Degrees
        result = self.default_robot.update_position(10, forward=True)
        self.assertTrue(result)
        mock_move.assert_called_with(Degrees(45), 10)
        self.assertEqual(self.default_robot.position, Position(5, 5))


if __name__ == "__main__":
    unittest.main()
