class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for i in range(n)]
        posDiag = set()
        negDiag = set()
        cols = set()
        res = []
        def dfs(rows):
            if rows == n:
                oneRow = ["".join(row) for row in board]
                res.append(oneRow.copy())
                return
            for c in range(n):
                if c in cols or c + rows in posDiag or c - rows in negDiag:
                    continue
                cols.add(c)
                posDiag.add(c + rows)
                negDiag.add(c - rows)
                board[rows][c] = "Q"
                dfs(rows + 1)
                cols.remove(c)
                posDiag.remove(c + rows)
                negDiag.remove(c - rows)
                board[rows][c] = "."
        dfs(0)
        return res