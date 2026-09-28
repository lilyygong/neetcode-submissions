class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(startIndex, path):
            if startIndex == len(s):
                res.append(path.copy())
                return
            for edge in range(startIndex, len(s)):
                temp = s[startIndex:edge + 1]
                revTemp = temp[::-1]
                if temp == revTemp:
                    path.append(temp)
                    dfs(edge + 1, path)
                    path.pop()
        dfs(0, [])
        return res
            