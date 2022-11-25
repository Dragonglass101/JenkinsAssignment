#!/usr/bin/python3
# Failing Test case for factorial

import unittest
from modulus import return_modulus


class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(return_modulus(19,3), 2)

    def testCase2(self):
        self.assertEqual(return_modulus(7,6), 3)


if __name__ == '__main__':
    unittest.main()
