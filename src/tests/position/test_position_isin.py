import unittest
from main.world_objects.position import Position


class MyTestCase(unittest.TestCase):
    def test_position_inside_bounds(self):
            top_left = Position(-100, 200)
            bottom_right = Position(100, -200)
            pos = Position(0, 0)
            self.assertTrue(pos.is_in(top_left, bottom_right), "Position (0, 0) should be inside the bounds")

    def test_position_on_boundary(self):
        top_left = Position(-100, 200)
        bottom_right = Position(100, -200)
        pos = Position(-100, 200)
        self.assertTrue(pos.is_in(top_left, bottom_right), "Position (-100, 200) should be on the boundary and thus inside the bounds")
        pos = Position(100, -200)
        self.assertTrue(pos.is_in(top_left, bottom_right), "Position (100, -200) should be on the boundary and thus inside the bounds")
        pos = Position(-100, -200)
        self.assertTrue(pos.is_in(top_left, bottom_right), "Position (-100, -200) should be on the boundary and thus inside the bounds")
        pos = Position(100, 200)
        self.assertTrue(pos.is_in(top_left, bottom_right), "Position (100, 200) should be on the boundary and thus inside the bounds")

    def test_position_outside_bounds(self):
        top_left = Position(-100, 200)
        bottom_right = Position(100, -200)
        pos = Position(-101, 0)
        self.assertFalse(pos.is_in(top_left, bottom_right), "Position (-101, 0) should be outside the bounds")
        pos = Position(0, 201)
        self.assertFalse(pos.is_in(top_left, bottom_right), "Position (0, 201) should be outside the bounds")
        pos = Position(101, 0)
        self.assertFalse(pos.is_in(top_left, bottom_right), "Position (101, 0) should be outside the bounds")
        pos = Position(0, -201)
        self.assertFalse(pos.is_in(top_left, bottom_right), "Position (0, -201) should be outside the bounds")

    def test_position_edge_cases(self):
        top_left = Position(-100, 200)
        bottom_right = Position(100, -200)
        pos = Position(-100, 199)
        self.assertTrue(pos.is_in(top_left, bottom_right), "Position (-100, 199) should be inside the bounds")
        pos = Position(100, -199)
        self.assertTrue(pos.is_in(top_left, bottom_right), "Position (100, -199) should be inside the bounds")
        pos = Position(-99, 200)
        self.assertTrue(pos.is_in(top_left, bottom_right), "Position (-99, 200) should be inside the bounds")
        pos = Position(99, -200)
        self.assertTrue(pos.is_in(top_left, bottom_right), "Position (99, -200) should be inside the bounds")


if __name__ == '__main__':
    unittest.main()
