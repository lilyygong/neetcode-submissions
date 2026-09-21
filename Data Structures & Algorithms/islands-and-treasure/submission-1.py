from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        bfs_treasure = deque()
        level_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    bfs_treasure.append([i, j])
        while len(bfs_treasure) > 0:
            level_count += 1
            level_size = len(bfs_treasure)
            for _ in range(level_size):
                cell = bfs_treasure.popleft()
                if cell[0] + 1 < len(grid) and grid[cell[0] + 1][cell[1]] == 2147483647:
                    grid[cell[0] + 1][cell[1]] = level_count
                    bfs_treasure.append([cell[0] + 1, cell[1]])
                if cell[1] + 1 < len(grid[0]) and grid[cell[0]][cell[1] + 1] == 2147483647:
                    grid[cell[0]][cell[1] + 1] = level_count
                    bfs_treasure.append([cell[0], cell[1] + 1])
                if cell[0] - 1 >= 0 and grid[cell[0] - 1][cell[1]] == 2147483647:
                    grid[cell[0] - 1][cell[1]] = level_count
                    bfs_treasure.append([cell[0] - 1, cell[1]])
                if cell[1] - 1 >= 0 and grid[cell[0]][cell[1] - 1] == 2147483647:
                    grid[cell[0]][cell[1] - 1] = level_count
                    bfs_treasure.append([cell[0], cell[1] - 1])