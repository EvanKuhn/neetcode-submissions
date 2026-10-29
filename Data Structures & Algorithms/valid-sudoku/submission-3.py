
def check_line(
    board: List[List[str]], 
    i_range: List[int], 
    j_range: List[int],
) -> bool:
    counts = [0] * 9
    index_pairs = list(zip(i_range, j_range))
    for i, j in index_pairs:
        val = board[i][j]
        if val == ".":
            continue
        num: int = int(val)
        counts[num-1] += 1
        if counts[num-1] > 1:
            return False
    return True


def check_row(board: List[List[str]], i: int) -> bool:
    return check_line(board, [i]*9, list(range(0,9)))

def check_col(board: List[List[str]], i: int) -> bool:
    return check_line(board, list(range(0,9)), [i]*9)


def check_square(board: List[List[str]], i: int) -> bool:
    i_base = (i // 3) * 3
    i_range = ([i_base] * 3) + ([i_base+1] * 3) + ([i_base+2] * 3)

    j_base = (i % 3) * 3
    j_range = [j_base, j_base+1, j_base+2] * 3

    return check_line(board, i_range, j_range)


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            if not check_row(board, i):
                return False
            if not check_col(board, i):
                return False
            if not check_square(board, i):
                return False
        return True
            
