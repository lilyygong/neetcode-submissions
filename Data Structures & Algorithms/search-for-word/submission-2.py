class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def dfs(row, col, i):
            if i == len(word):
                return True
            if row >= len(board) or col >= len(board[0]) or row < 0 or col < 0 or board[row][col] != word[i] or (row, col) in visited:
                return False
            visited.add((row, col))
            up = dfs(row + 1, col, i + 1)
            right = dfs(row, col + 1, i + 1)
            down = dfs(row - 1, col, i + 1)
            left = dfs(row, col - 1, i + 1)
            visited.remove((row, col))
            return up or right or down or left

        for row in range(len(board)):
                for col in range(len(board[0])):
                    if dfs(row, col, 0):
                        return True
        return False

