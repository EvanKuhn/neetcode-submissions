from enum import IntEnum
from collections import namedtuple, deque
from typing import List

Point = namedtuple('Point', ['x', 'y'])

class Cell(IntEnum):
    WATER = -1
    TREASURE = 0
    LAND_INF = 2147483647

class Solution:
    def find_chests(self, grid: List[List[int]]) -> List[Point]:
        results = []
        for x in range(0,len(grid)):
            for y in range(0,len(grid[0])):
                if grid[x][y] == Cell.TREASURE:
                    results.append(Point(x,y))
        return results


    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        xlen = len(grid)
        ylen = len(grid[0])
        chests: List[Point] = self.find_chests(grid)
        to_search = deque([(c,0) for c in chests])
        visited = set()

        while to_search:
            loc, curdist = to_search.popleft()
            x,y = loc

            # Skip invalid locations, visited locations, and water
            if not (0 <= x < xlen and 0 <= y < ylen):
                continue
            if loc in visited:
                continue
            if grid[x][y] == Cell.WATER:
                continue

            # Mark cell as visited
            visited.add(loc)

            # If on land, update the min distance
            if grid[x][y] > 0:
                # Stop if the min distance is already as good or 
                # better than curdist
                if curdist >= grid[x][y]:
                    continue
                grid[x][y] = min(grid[x][y], curdist)

            # Visit neighbors
            to_search.append((Point(x+1, y), curdist+1))
            to_search.append((Point(x-1, y), curdist+1))
            to_search.append((Point(x, y+1), curdist+1))
            to_search.append((Point(x, y-1), curdist+1))