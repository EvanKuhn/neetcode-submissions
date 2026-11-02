
class Solution:
    def visit_surrounding_land(
        self, 
        grid: List[List[str]], 
        visited: List[List[bool]], 
        x: int, 
        y: int,
    ) -> None:
        # Skip invalid x,y coordinates
        if not (0 <= x < (len(grid))):
            return
        if not (0 <= y < (len(grid[0]))):
            return
        
        # Skip water, or visited cells
        if grid[x][y] == "0" or visited[x][y]:
            return

        # Mark cell as visited
        visited[x][y] = True

        # Visit neighbors
        self.visit_surrounding_land(grid, visited, x+1, y)
        self.visit_surrounding_land(grid, visited, x-1, y)
        self.visit_surrounding_land(grid, visited, x, y+1)
        self.visit_surrounding_land(grid, visited, x, y-1)


    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
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
                island_count += 1
                self.visit_surrounding_land(grid, visited, x, y)
        
        return island_count
                
