
class Solution:
    def visit_surrounding_land(
        self, 
        grid: List[List[str]], 
        visited: List[List[bool]], 
        x: int, 
        y: int,
    ) -> int:
        # Skip invalid x,y coordinates
        if not (0 <= x < (len(grid))):
            return 0
        if not (0 <= y < (len(grid[0]))):
            return 0
        
        # Skip water, or visited cells
        if grid[x][y] == 0 or visited[x][y]:
            return 0

        # Mark cell as visited
        visited[x][y] = True
        area = 1

        # Visit neighbors
        area += self.visit_surrounding_land(grid, visited, x+1, y)
        area += self.visit_surrounding_land(grid, visited, x-1, y)
        area += self.visit_surrounding_land(grid, visited, x, y+1)
        area += self.visit_surrounding_land(grid, visited, x, y-1)
        return area


    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        max_area = 0
        xlen: int = len(grid)
        ylen: int = len(grid[0])
        visited: List[List[bool]] = [([False] * ylen) for _ in range(0,xlen)] 

        # Visit each grid location
        for x in range(0, xlen):
            for y in range(0, ylen):
                # Skip water, or visited cells
                if grid[x][y] == "0" or visited[x][y]:
                    continue

                # Increment the island count and tag all neighboring
                # land cells as visited.
                area = self.visit_surrounding_land(grid, visited, x, y)
                max_area = max(area, max_area)
        
        return max_area

