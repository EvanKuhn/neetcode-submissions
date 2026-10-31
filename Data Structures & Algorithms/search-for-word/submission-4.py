class Solver:
    def __init__(self, board: List[List[str]], word: str) -> None:
        self.board = board
        self.word = word
        #self.seen = set()
        self.x_len = len(board)
        self.y_len = len(board[0])

    def search(self, x: int, y: int) -> bool:
        return self._search(x, y, self.word, path=[], seen=set())

    def _search(self, x: int, y: int, word: str, path: List[tuple[int,int]], seen: set[tuple[int,int]]) -> bool:
        #print(f"_search(x={x}, y={y}, word={word})")
        
        # Empty word: success!
        if not word:
            return True

        # We matched the last char
        if len(word) == 1 and self.board[x][y] == word[0]:
            return True

        # Ensure board location matches first char of word
        if self.board[x][y] != word[0]:
            return False

        # Record that we visited this square
        curloc = (x,y)
        assert curloc not in seen
        path.append(curloc)
        seen.add(curloc)

        # Search adjacent squares that we haven't seen
        status = False
        adjacent = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
        for loc in adjacent:
            if loc not in seen and self._is_valid(loc):
                if self._search(loc[0], loc[1], word[1:], path, seen):
                    status = True
                    break
    
        # Remove current location and return
        path.pop()
        seen.remove(curloc)
        return status
    
    def _is_valid(self, loc: tuple[int,int]) -> bool:
        x, y = loc
        return (0 <= x < self.x_len) and (0 <= y < self.y_len)


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for x in range(0,len(board)):
            for y in range(0, len(board[0])):
                solver = Solver(board, word)
                if solver.search(x, y):
                    return True
        return False
