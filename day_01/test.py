#!/usr/bin/env python3.6

import unittest
from resolve import resolve_p1, resolve_p2


class Day01Part1Test(unittest.TestCase):

    def test_two_eq(self):
        self.assertEqual(resolve_p1('1122'), 3)

    def test_all_eq(self):
        self.assertEqual(resolve_p1('1111'), 4)

    def test_non_eq(self):
        self.assertEqual(resolve_p1('1234'), 0)

    def test_tail_eq_head(self):
        self.assertEqual(resolve_p1('91212129'), 9)


class Day01Part2Test(unittest.TestCase):

    def test_one(self):
        self.assertEqual(resolve_p2('1212'), 6)

    def test_two(self):
        self.assertEqual(resolve_p2('1221'), 0)

    def test_three(self):
        self.assertEqual(resolve_p2('123425'), 4)

    def test_four(self):
        self.assertEqual(resolve_p2('123123'), 12)

    def test_five(self):
        self.assertEqual(resolve_p2('12131415'), 4)


if __name__ == '__main__':
    unittest.main()
