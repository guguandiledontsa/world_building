import unittest
from unittest.mock import patch
from main.robot import Robot
from main.position import Position
from main.direction import Direction


class MyTestCase(unittest.TestCase):
    def setUp(self):
        # Setup default test robot
        self.default_robot = Robot(name="TestBot")

    def test_default_robot_initialization(self):
        robot = self.default_robot
        self.assertEqual(robot.name, "TestBot")
        self.assertEqual(robot.position, Position(0, 0))
        self.assertEqual(robot.current_direction, Direction.NORTH)
        self.assertEqual(robot.status, "Ready")
        self.assertEqual(robot.history, [])
        self.assertEqual(robot.type, "basic")
        self.assertEqual(robot.shot_damage, 1)
        self.assertEqual(robot.initial_ammo, 5)
        self.assertEqual(robot.shield_max, 5)
        self.assertEqual(robot.ammo, 5)
        self.assertEqual(robot.shield_level, 5)
        self.assertEqual(robot.repair_delay, 5)
        self.assertEqual(robot.reload_delay, 5)
        self.assertFalse(robot.is_reloading)
        self.assertFalse(robot.is_repairing)

    def test_set_attributes_based_on_type(self):
        robot_types = {
            "scout": (1, 5, 1, 2, 2),
            "sniper": (5, 1, 1, 4, 5),
            "tank": (3, 5, 5, 5, 3),
            "assault": (2, 3, 3, 3, 3),
            "support": (1, 4, 2, 3, 2),
            "basic": (1, 5, 5, 5, 5)  # Default type
        }

        for robot_type, attributes in robot_types.items():
            with self.subTest(robot_type=robot_type):
                robot = Robot(name="TestBot", type=robot_type)
                robot.set_attributes_based_on_type()
                self.assertEqual(robot.shot_damage, attributes[0])
                self.assertEqual(robot.initial_ammo, attributes[1])
                self.assertEqual(robot.shield_max, attributes[2])
                self.assertEqual(robot.repair_delay, attributes[3])
                self.assertEqual(robot.reload_delay, attributes[4])
                self.assertEqual(robot.ammo, attributes[1])
                self.assertEqual(robot.shield_level, attributes[2])

    def test_update_position_forward(self):
        self.default_robot.position = Position(0, 0)
        self.default_robot.current_direction = Direction.NORTH
        result = self.default_robot.update_position(3, forward=True)
        self.assertTrue(result)
        self.assertEqual(self.default_robot.position, Position(0, 3))

    def test_update_position_backward(self):
        self.default_robot.position = Position(0, 0)
        self.default_robot.current_direction = Direction.NORTH
        result = self.default_robot.update_position(3, forward=False)
        self.assertTrue(result)
        self.assertEqual(self.default_robot.position, Position(0, -3))

    @patch('main.position.Position.move')
    def test_update_position_with_mock(self, mock_move):
        mock_move.return_value = Position(5, 5)
        self.default_robot.position = Position(0, 0)
        self.default_robot.current_direction = Direction.NORTH
        result = self.default_robot.update_position(10, forward=True)
        self.assertTrue(result)
        mock_move.assert_called_with(Direction.NORTH, 10)
        self.assertEqual(self.default_robot.position, Position(5, 5))

    def test_str_method(self):
        robot = self.default_robot
        expected_str = ("Name: TestBot, Position: Position(x=0, y=0), Direction: Direction.NORTH, "
                        "Status: Ready, Shield Level: 5, Ammo: 5, Type: basic")
        self.assertEqual(str(robot), expected_str)

    def test_initial_ammo(self):
        robot = Robot(name="TestBot", type="sniper")
        self.assertEqual(robot.ammo, 1)

    def test_shield_max(self):
        robot = Robot(name="TestBot", type="tank")
        self.assertEqual(robot.shield_level, 5)

    def test_repair_and_reload_delays(self):
        robot = Robot(name="TestBot", type="support")
        self.assertEqual(robot.repair_delay, 3)
        self.assertEqual(robot.reload_delay, 2)

    def test_edge_case(self):
        robot = Robot(name="TestBot", type="unknown")
        robot.set_attributes_based_on_type()
        self.assertEqual(robot.shot_damage, 1)  # Default values
        self.assertEqual(robot.initial_ammo, 5)
        self.assertEqual(robot.shield_max, 5)
        self.assertEqual(robot.repair_delay, 5)
        self.assertEqual(robot.reload_delay, 5)


if __name__ == '__main__':
    unittest.main()
