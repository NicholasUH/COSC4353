import unittest
import sys
sys.path.append('src')
from get_perfect_number import get_factors, is_perfect_number_two_times, is_perfect_number

class TestGetPerfectNumber(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_get_factors_even(self):
        self.assertEqual([1, 2, 3, 6], get_factors(6))

    def test_get_factors_odd(self):
        self.assertEqual([1, 5], get_factors(5))
    
    def test_is_perfect_number_two_times_even(self):
        self.assertTrue(is_perfect_number_two_times(6, 12))
    
    def test_is_perfect_number_two_times_odd(self):
        self.assertFalse(is_perfect_number_two_times(5, 12))
    
    def test_is_perfect_number(self):
        self.assertTrue(is_perfect_number(6))

    def test_is_not_perfect_number(self):
        self.assertFalse(is_perfect_number(5))
