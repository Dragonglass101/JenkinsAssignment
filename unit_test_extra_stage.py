#!/usr/bin/python3
# Passing Test case for checking factorial of numbers

import unittest
from modulus import return_modulus


class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(return_modulus(5,2), 1)

    def testCase2(self):
        self.assertEqual(return_modulus(10,3), 2)

    def testCase3(self):
        self.assertEqual(return_modulus(6,2), 0)


if __name__ == '__main__':
    unittest.main()