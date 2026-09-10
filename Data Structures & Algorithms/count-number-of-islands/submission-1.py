class Solution:

    def tag_adjacent_cells(
        self, x: 
        int, y: 
        int, 
        grid: List[List[str]], 
        seen: Set[Tuple[int,int]],
    ) -> None:
        '''
        Given an x,y coordinate in the grid that is a 1, look for all 
        adjacent coordinates that hold a 1, and mark them as seen.
        '''
        coords = [(x,y)]

        while coords:
            # Get next coordinate, record that we've seen it
            c = coords.pop()
            if c in seen:
                continue

            # Record that we saw this coordinate
            seen.add(c)

            # If 0, don't look further
            i, j = c
            if grid[i][j] == "0":
                continue

            # Look for adjacent coordinates 
            for adj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                x1, y1 = adj
                if x1 < 0 or x1 >= len(grid):
                    continue
                if y1 < 0 or y1 >= len(grid[x1]):
                    continue
                coords.append(adj)

    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        islands = 0

        # Look for the next 1 that we haven't seen
        for x in range(0, len(grid)):
            for y in range(0, len(grid[x])):
                # Skip this cell if we've seen it
                if (x,y) in seen:
                    continue

                # If this is a 1, look for all adjacent cells
                if grid[x][y] == "1":
                    self.tag_adjacent_cells(x, y, grid, seen)
                    islands += 1

        return islands
