import unittest
from src.main.world import World
from src.main.world_objects.position import Position
from src.main.world_objects.degrees import Degrees


class TestWorld(unittest.TestCase):

    def setUp(self):
        self.world = World()

    def test_spawn_robot(self):
        self.world.spawn_robot(
            name="TestBot", position=Position(0, 0), direction=Degrees(90), type="scout"
        )
        robot = self.world.get_robot(name="TestBot")
        self.assertIsNotNone(robot)
        self.assertEqual(robot.position, Position(0, 0))
        self.assertEqual(robot.direction.angle, 90)
        self.assertEqual(robot.type, "scout")

    def test_spawn_robot_with_duplicate_name(self):
        self.world.spawn_robot(
            name="UniqueBot", position=Position(1, 1), direction=Degrees(45)
        )
        with self.assertRaises(ValueError):
            self.world.spawn_robot(
                name="UniqueBot", position=Position(2, 2), direction=Degrees(90)
            )

    def test_move_robot(self):
        self.world.spawn_robot(
            name="MoverBot", position=Position(0, 0), direction=Degrees(0)
        )
        self.world.move_robot(name="MoverBot", steps=10, forward=True)
        robot = self.world.get_robot(name="MoverBot")
        self.assertEqual(robot.position, Position(10, 0))

    def test_turn_robot_left(self):
        self.world.spawn_robot(
            name="TurnerBot", position=Position(0, 0), direction=Degrees(0)
        )
        self.world.turn_robot_left(name="TurnerBot")
        robot = self.world.get_robot(name="TurnerBot")
        self.assertEqual(
            robot.direction.angle, 270
        )  # Turned left from 0° to 270°

    def test_turn_robot_right(self):
        self.world.spawn_robot(
            name="RightTurnerBot", position=Position(0, 0), direction=Degrees(0)
        )
        self.world.turn_robot_right(name="RightTurnerBot")
        robot = self.world.get_robot(name="RightTurnerBot")
        self.assertEqual(
            robot.direction.angle, 90
        )  # Turned right from 0° to 90°

    def test_list_robots(self):
        self.world.spawn_robot(
            name="Bot1", position=Position(0, 0), direction=Degrees(0)
        )
        self.world.spawn_robot(
            name="Bot2", position=Position(1, 1), direction=Degrees(90)
        )
        self.assertIn("Bot1", self.world.list_robots())
        self.assertIn("Bot2", self.world.list_robots())


if __name__ == "__main__":
    unittest.main()
