class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        res = []
        def dfs(startIndex, dots, path):
            if dots == 4 and startIndex == len(s):
                res.append(".".join(path.copy()))
                return
            if dots > 4:
                return
            for i in range(startIndex, min(startIndex + 3, len(s))):
                if startIndex !=i and s[startIndex] == "0":
                    continue
                if int(s[startIndex:i+1]) < 256:
                    path.append(s[startIndex:i+1])
                    dfs(i+1, dots + 1, path)
                    path.pop()
        dfs(0, 0, [])
        return res