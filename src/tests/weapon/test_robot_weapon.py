import unittest
from src.main.world_objects.robot import Robot  # Adjust import path as needed

class FireTest(unittest.TestCase):
    def setUp(self):
        self.robot = Robot("CrashTestDummy")

    def test_ammo_initial(self):
        self.assertEqual(self.robot.weapon.ammo, 5)

    def test_ammo_after_fire(self):
        self.robot.shoot()  # Assuming fire method reduces ammo
        self.assertEqual(self.robot.weapon.ammo, 4)

    def test_ammo_depletion(self):
        for expected_ammo in range(4, 0, -1):
            self.robot.shoot()
            self.assertEqual(self.robot.weapon.ammo, expected_ammo)

    def test_ammo_to_no_bullets(self):
        for _ in range(4):
            self.robot.shoot()
        self.robot.shoot()  # Fire when ammo is 0
        self.assertEqual(self.robot.weapon.ammo, 0)

if __name__ == '__main__':
    unittest.main()
