class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(path, opens, close):
            if len(path) == n * 2:
                res.append("".join(path.copy()))
                return
            if close < n and close < opens:
                path.append(")")
                dfs(path, opens, close + 1)
                path.pop()
            if opens < n:
                path.append("(")
                dfs(path, opens + 1, close)
                path.pop()
        dfs([], 0, 0)
        return res