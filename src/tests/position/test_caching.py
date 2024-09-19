# import unittest
# from functools import lru_cache
# from time import sleep, time
# from math import sqrt
#
# # Function to be tested
# @lru_cache(maxsize=2)
# def expensive_function(x):
#     sleep(1)  # Simulating an expensive computation
#     return x * x
#
# class InvalidPositionError(Exception):
#     """Custom exception for invalid position coordinates."""
#     pass
#
# class Position:
#     def __init__(self, x, y):
#         if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
#             raise InvalidPositionError("Coordinates must be numeric.")
#         self.x = x
#         self.y = y
#
#     @lru_cache(maxsize=None)
#     def distance_to(self, other):
#         if not isinstance(other, Position):
#             raise ValueError("The argument must be a Position instance.")
#         return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
#
# class TestCacheBehavior(unittest.TestCase):
#
#     def setUp(self):
#         # Clear the caches before each test to ensure isolation
#         expensive_function.cache_clear()
#         self.pos1 = Position(1.0, 2.0)
#         self.pos2 = Position(4.0, 6.0)
#
#         # Clear the Position's cache
#         self.pos1.distance_to.cache_clear()
#
#     def test_expensive_function_cache_behavior(self):
#         # Test cache behavior for expensive_function
#         result1 = expensive_function(4)
#         self.assertEqual(result1, 16)
#
#         result2 = expensive_function(4)
#         self.assertEqual(result2, 16)
#         self.assertEqual(expensive_function.cache_info().hits, 1)
#
#         result3 = expensive_function(5)
#         self.assertEqual(result3, 25)
#         self.assertEqual(expensive_function.cache_info().currsize, 2)
#
#         # This call should evict the oldest entry (4)
#         result4 = expensive_function(6)
#         self.assertEqual(result4, 36)
#         self.assertEqual(expensive_function.cache_info().currsize, 2)
#
#     def test_position_distance_cache_behavior(self):
#         # Test cache behavior for Position's distance_to method
#         distance1 = self.pos1.distance_to(self.pos2)
#         self.assertEqual(distance1, sqrt((1.0 - 4.0) ** 2 + (2.0 - 6.0) ** 2))
#         self.assertEqual(self.pos1.distance_to.cache_info().hits, 0)
#
#         distance2 = self.pos1.distance_to(self.pos2)
#         self.assertEqual(distance2, distance1)
#         self.assertEqual(self.pos1.distance_to.cache_info().hits, 1)
#
#         # Adding a new Position to fill the cache
#         self.pos1.distance_to(Position(7.0, 8.0))
#         self.assertEqual(self.pos1.distance_to.cache_info().currsize, 2)
#
#         # Adding another new Position should evict the oldest entry
#         self.pos1.distance_to(Position(9.0, 10.0))
#         self.assertEqual(self.pos1.distance_to.cache_info().currsize, 2)
#
#     def test_cache_performance(self):
#         # Test performance for expensive_function
#         start_time = time()
#         expensive_function(3)
#         first_call_duration = time() - start_time
#
#         start_time = time()
#         expensive_function(3)
#         second_call_duration = time() - start_time
#         self.assertLess(second_call_duration, first_call_duration * 0.1)
#
#     def test_cache_clear(self):
#         # Fill the cache for expensive_function
#         expensive_function(1)
#         expensive_function(2)
#         self.assertEqual(expensive_function.cache_info().currsize, 2)
#
#         # Clear the cache
#         expensive_function.cache_clear()
#         self.assertEqual(expensive_function.cache_info().currsize, 0)
#
#         # Fill the cache for Position's distance_to
#         self.pos1.distance_to(self.pos2)
#         self.pos1.distance_to(Position(7.0, 8.0))
#         self.assertEqual(self.pos1.distance_to.cache_info().currsize, 2)
#
#         # Clear the cache
#         self.pos1.distance_to.cache_clear()
#         self.assertEqual(self.pos1.distance_to.cache_info().currsize, 0)
#
# if __name__ == '__main__':
#     unittest.main()
