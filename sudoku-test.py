import unittest
from sudoku import check_pos

board = [
        [7, 2, 3, 0, 0, 0, 1, 5, 9],
        [6, 0, 0, 3, 0, 2, 0, 0, 8],
        [8, 0, 0, 0, 1, 0, 0, 0, 2],
        [0, 7, 0, 6, 5, 4, 0, 2, 0],
        [0, 0, 4, 2, 0, 7, 3, 0, 0],
        [0, 5, 0, 9, 3, -1, 0, 4, 0],
        [5, 0, 0, 0, 7, 0, 0, 0, 3],
        [4, 0, 0, 1, 0, 3, 0, 0, 6],
        [9, 3, 2, 0, 0, 0, 7, 1, 4]]
# Test positional function against above testing board.


class SudokoTestCase(unittest.TestCase):
    def test_empty_square(self):
        # Test an empty square
        col = 1
        row = 1
        testing = True
        result = check_pos(col, row, board, testing)
        self.assertTrue(result)

    def test_filled_square(self):
        # Test a square permenent square.
        col = 0
        row = 0
        testing = True
        result = check_pos(col, row, board, testing)
        self.assertFalse(result)

    def test_played_square(self):
        # Test a square that player played on.
        col = 5
        row = 5
        testing = True
        result = check_pos(col, row, board, testing)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

