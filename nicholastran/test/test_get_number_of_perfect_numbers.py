import unittest
import sys
sys.path.append('src')
from get_number_of_perfect_numbers import get_number_of_perfect_numbers

class TestGetNumberOFPerfectNumbers(unittest.TestCase):
    def test_get_all_perfect_numbers_exist(self):
        self.assertEqual(2, get_number_of_perfect_numbers(30))

    def test_get_all_perfect_numbers_does_not_exist(self):
        self.assertEqual(0, get_number_of_perfect_numbers(1))
        