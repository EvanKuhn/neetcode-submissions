from enum import IntEnum
from collections import deque, namedtuple

Point = namedtuple('Point', ['x', 'y'])

class Cell(IntEnum):
    EMPTY = 0
    FRESH = 1
    ROTTEN = 2

class Solution:
    def find_rotten_fruit(self, grid: List[List[int]]) -> List[Point]:
        results = []
        for x in range(0,len(grid)):
            for y in range(0,len(grid[0])):
                if grid[x][y] == Cell.ROTTEN:
                    results.append(Point(x,y))
        return results

    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Run a BFS from all rotten fruit
        # Collect visited cells
        # Check if all fruit has been visited

        max_minutes = 0
        xlen = len(grid)
        ylen = len(grid[0])
        rotten = []
        num_fresh = 0

        # Collect locations of rotten fruit, and number of fresh fruit
        for x in range(0,xlen):
            for y in range(0,ylen):
                if grid[x][y] == Cell.FRESH:
                    num_fresh += 1
                if grid[x][y] == Cell.ROTTEN:
                    rotten.append(Point(x,y))

        # Prepare for breadth-first search of grid
        to_visit = deque([(loc,0) for loc in rotten]) # Pairs of (location, minutes)
        visited_fresh = set()
        visited_rotten = set()

        while to_visit:
            # Get next location
            loc, minutes = to_visit.popleft()
            x,y = loc

            # Skip if invalid, etc
            if not (0 <= x < xlen):
                continue
            if not (0 <= y < ylen):
                continue
            if loc in visited_fresh or loc in visited_rotten:
                continue
            if grid[x][y] == Cell.EMPTY:
                continue

            # Keep track of visited cells
            if grid[x][y] == Cell.FRESH:
                visited_fresh.add(loc)
            else:
                assert grid[x][y] == Cell.ROTTEN
                visited_rotten.add(loc)

            # Keep track of minutes
            max_minutes = max(max_minutes, minutes)

            to_visit.append((Point(x+1, y), minutes+1))
            to_visit.append((Point(x-1, y), minutes+1))
            to_visit.append((Point(x, y+1), minutes+1))
            to_visit.append((Point(x, y-1), minutes+1))

        # Check if all land cells were visited
        if len(visited_fresh) < num_fresh:
            return -1
        return max_minutes



