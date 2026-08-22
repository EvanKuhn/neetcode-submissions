from collections import defaultdict

class Counter:
    '''
    Helper class to keep track of the numbers in a row, column, or
    square. Use add() to add a number (as a singl-char string); this
    will return False if a duplicate was found.

    The intention is to maintain a Counter for each row, column, and
    square. Then iterate over all elements in the sudoku, and add them
    to the Counters. If any row/column/square contains a duplicate number,
    we know the puzzle is invalid.
    '''

    def __init__(self):
        self._counts = defaultdict(int)
        self._valid = True

    def add(self, n: str) -> bool:
        '''
        Add a number (as a single-char string). 
        - Return True if the number was NOT seen (valid puzzle)
        - Return False if the number was seen (invalid puzzle) 
        '''
        assert '0' <= n <= '9', f"String '{n}' not in range 0-9"
        self._counts[n] += 1
        #print(self._counts)
        if self._counts[n] > 1:
            self._valid = False
        return self._valid

    def valid(self) -> bool:
        return self._valid
    

def loc_to_square_index(x: int, y: int) -> int:
    '''
    Given an (x,y) coordinate, determine which of the 9 "squares" contains
    that coordinate, and return the integer for that square. We'll count 
    count across and down:

            1   2   3
            4   5   6
            7   8   9

    Keep in mind that the 'y' value actually goes down, though it doesn't 
    really matter.
    '''
    return 3 * (x // 3) + (y // 3)


def print_board(board: List[List[str]]) -> None:
    for x in range(0,9):
        for y in range(0,9):
            c = board[x][y]
            print(f"{c} ", end='')
        print()


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #print_board(board)

        row_counters = []
        col_counters = []
        sqr_counters = []

        for i in range(0,9):
            row_counters.append(Counter())
            col_counters.append(Counter())
            sqr_counters.append(Counter())

        for x in range(0,9):
            for y in range(0,9):
                c = board[x][y]
                if c == '.':
                    continue
                #print(f"Adding [{x}, {y}]={c}")
                i = loc_to_square_index(x, y)
                if not row_counters[x].add(c):
                    #print("row failure!")
                    return False
                if not col_counters[y].add(c):
                    #print("col failure!")
                    return False
                if not sqr_counters[i].add(c):
                    #print(f"square[{i}] failure!")
                    return False

        return True
        