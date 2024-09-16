import unittest


from main.world_objects.degrees import Degrees


class MyTestCase(unittest.TestCase):
    def test_angle_normalization(self):
        a = Degrees(400)
        self.assertEqual(a.angle, 40)
        a.angle = -30
        self.assertEqual(a.angle, 330)

        a.angle = 720
        self.assertEqual(a.angle, 0)

        a.angle = -750
        self.assertEqual(a.angle, 330)

    def test_angle_normalize(self):
        a = Degrees(-10)
        self.assertEqual(a.angle, 350)

        a.angle = 366
        self.assertEqual(a.angle, 6)

    def test_degrees(self):
        a = Degrees(10)
        self.assertEqual(a.angle, 10)

        a.angle = 30
        self.assertEqual(a.angle, 30)

    def test_degrees_edge(self):
        a = Degrees(360)
        self.assertEqual(a.angle, 10)

if __name__ == '__main__':
    unittest.main()
