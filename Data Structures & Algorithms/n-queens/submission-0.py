class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = set()
        posDiag = set() # (r+c)
        negDiag = set() # (r-c)
        board = [["."] * n for i in range (n)]
        def dfs(startIndex):
            if startIndex == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n): # iterate every position in the curr row
                if c in col or (startIndex + c) in posDiag or (startIndex - c) in negDiag:
                    continue
                col.add(c)
                posDiag.add(startIndex + c)
                negDiag.add(startIndex - c)
                board[startIndex][c] = "Q"

                dfs(startIndex + 1)

                col.remove(c)
                posDiag.remove(startIndex + c)
                negDiag.remove(startIndex - c)
                board[startIndex][c] = "."
        dfs(0)
        return res


