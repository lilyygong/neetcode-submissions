from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_queue = deque()
        total_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    total_islands += 1
                    island_queue.append([i, j])
                    self.bfs(island_queue, grid)
        return total_islands
    
    def bfs(self, island_queue, grid):
        while len(island_queue) > 0:
            cell = island_queue.popleft()
            if cell[0] + 1 < len(grid) and grid[cell[0] + 1][cell[1]] == "1":
                grid[cell[0] + 1][cell[1]] = "0" # visit it
                island_queue.append([cell[0] + 1, cell[1]])
            if cell[1] + 1 < len(grid[0]) and grid[cell[0]][cell[1] + 1] == "1":
                grid[cell[0]][cell[1] + 1] = "0" # visit it
                island_queue.append([cell[0], cell[1] + 1])
            if cell[0] - 1 >= 0 and grid[cell[0] - 1][cell[1]] == "1":
                grid[cell[0] - 1][cell[1]] = "0" # visit it
                island_queue.append([cell[0] - 1, cell[1]])
            if cell[1] - 1 >= 0 and grid[cell[0]][cell[1] - 1] == "1":
                grid[cell[0]][cell[1] - 1] = "0" # visit it
                island_queue.append([cell[0], cell[1] - 1])

# loop through the matrix to find island
# use bfs to consume the entire island
# need to mark the spots as visited to avoid counting twice
# we can overwrite the 1 as a 2 or 0

