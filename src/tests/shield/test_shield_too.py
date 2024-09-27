import unittest
import time

from src.main.world_objects.robot import Robot


class TestRobotShield(unittest.TestCase):

    def setUp(self):
        self.robot = Robot("CrashTestDummy")

    def test_initial_shield(self):
        self.assertEqual(self.robot.shield_level(), 5)

    def test_damage_shield(self):
        self.robot.damage_shield(1)
        self.assertEqual(self.robot.shield_level(), 4)

    def test_damage_all(self):
        for _ in range(5):
            self.robot.damage_shield(1)
        self.assertEqual(self.robot.shield_level(), 0)

    def test_damage_overkill(self):
        for _ in range(7):
            self.robot.damage_shield(1)
        self.assertEqual(self.robot.shield_level(), 0)

    def test_repair_shield(self):
        self.robot.damage_shield(1)
        self.assertEqual(self.robot.shield_level(), 4)
        self.robot.repair_shield()
        time.sleep(6)  # Wait for repair to complete
        self.assertEqual(self.robot.shield_level(), 5)


if __name__ == "__main__":
    unittest.main()
