#!/usr/bin/env python3.6

import unittest
from resolve import resolve_part1, resolve_part2


class Day02Test(unittest.TestCase):

    def test_spreadsheet_part1(self):
        spreadsheet = [
            [5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]
        ]
        self.assertEqual(resolve_part1(spreadsheet), 18)

    def test_spreadsheet_part2(self):
        spreadsheet = [
            [5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]
        ]
        self.assertEqual(resolve_part2(spreadsheet), 9)


if __name__ == '__main__':
    unittest.main()
