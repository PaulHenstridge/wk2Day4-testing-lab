import unittest

from src.compare import compare


class TestCompare(unittest.TestCase):
    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("3 is greater than 1", compare(3, 1))

    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("31 is less than 3", compare(1, 3))

    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("nums are equal", compare(3, 3))
