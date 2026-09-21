from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_queue = deque()
        fresh_oranges = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    rotten_queue.append([i, j])
                if grid[i][j] == 1:
                    fresh_oranges += 1
        total_mins = 0
        while len(rotten_queue) > 0 and fresh_oranges > 0:
            total_mins += 1
            level_size = len(rotten_queue)
            for _ in range(level_size):
                node = rotten_queue.popleft()
                if node[0] + 1 <= len(grid) - 1 and grid[node[0] + 1][node[1]] == 1:
                    fresh_oranges -= 1
                    grid[node[0] + 1][node[1]] = 2
                    rotten_queue.append([node[0]+1, node[1]])
                if node[1] + 1 <= len(grid[0]) - 1 and grid[node[0]][node[1] + 1] == 1:
                    fresh_oranges -= 1
                    grid[node[0]][node[1] + 1] = 2
                    rotten_queue.append([node[0], node[1]+1])
                if node[0] - 1 >= 0 and grid[node[0] - 1][node[1]] == 1:
                    fresh_oranges -= 1
                    grid[node[0] - 1][node[1]] = 2
                    rotten_queue.append([node[0] - 1, node[1]])
                if node[1] - 1 >= 0 and grid[node[0]][node[1] - 1] == 1:
                    fresh_oranges -= 1
                    grid[node[0]][node[1] - 1] = 2
                    rotten_queue.append([node[0], node[1] - 1])
        if fresh_oranges > 0:
            return -1
        return total_mins

