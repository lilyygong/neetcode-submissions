class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(startIndex, path):
            if len(path) == k:
                res.append(path.copy())
                return
            if startIndex > n:
                return
            print(startIndex, path)
            path.append(startIndex)
            dfs(startIndex + 1, path)
            path.pop()
            dfs(startIndex + 1, path)
        dfs(1, [])
        return res