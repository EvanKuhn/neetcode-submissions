class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [['Q']]
        return self._solve(n, [])


    def _solve(self, n: int, existing: List[str]) -> List[List[str]]:
        results = []

        # Consider the next row. Place the queen in each position and recurse.
        for i in range(0, n):
            row = ("." * i) + 'Q' + ("." * (n-i-1))
            updated_rows = existing + [row]
            if self.last_row_valid(updated_rows):
                if len(updated_rows) == n:
                    results.append(updated_rows)
                else:
                    results.extend(self._solve(n, updated_rows))

        return results


    def last_row_valid(self, rows: List[str]) -> bool:
        nrows = len(rows)
        ncols = len(rows[0])

        # Check if queen in last row conflicts with any previous rows
        ci = rows[-1].index('Q')
        for ri in range(0, nrows-1):
            if rows[ri][ci] == "Q":
                return False

        # Check diagonals just for the queen in the last row
        ri = nrows-1

        r, c = ri-1, ci+1
        while (0 <= r < nrows) and (0 <= c < ncols):
            if rows[r][c] == "Q":
                return False
            r, c = r-1, c+1

        r, c = ri-1, ci-1
        while (0 <= r < nrows) and (0 <= c < ncols):
            if rows[r][c] == "Q":
                return False
            r, c = r-1, c-1

        return True



    # This is too inefficient. No need to check all rows every time. 
    # Just check the last row
    def rows_valid(self, rows: List[str]) -> bool:
        nrows = len(rows)
        ncols = len(rows[0])
        col_count = defaultdict(int)

        for ri in range(0,nrows):
            # Check one queen per column
            row = rows[ri]
            ci = row.index("Q")
            col_count[ci] += 1
            if col_count[ci] > 1:
                return False

            # Check diagonals
            r, c = ri+1, ci+1
            while (0 <= r < nrows) and (0 <= c < ncols):
                if rows[r][c] == "Q":
                    return False
                r, c = r+1, c+1

            r, c = ri+1, ci-1
            while (0 <= r < nrows) and (0 <= c < ncols):
                if rows[r][c] == "Q":
                    return False
                r, c = r+1, c-1
            
            r, c = ri-1, ci+1
            while (0 <= r < nrows) and (0 <= c < ncols):
                if rows[r][c] == "Q":
                    return False
                r, c = r-1, c+1

            r, c = ri-1, ci-1
            while (0 <= r < nrows) and (0 <= c < ncols):
                if rows[r][c] == "Q":
                    return False
                r, c = r-1, c-1

        return True
