class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(startIndex, path):
            if startIndex == len(s):
                res.append(path.copy())
                return
            for i in range(startIndex, len(s)):
                temp = s[startIndex:i + 1]
                rev = temp[::-1]
                if rev == temp:
                    path.append(temp)
                    dfs(i + 1, path)
                    path.pop()
        dfs(0, [])
        return res