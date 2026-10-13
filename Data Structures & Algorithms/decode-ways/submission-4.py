class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(startIndex):
            if startIndex == len(s):
                memo[startIndex] = 1
                return 1
            if s[startIndex] == '0':
                memo[startIndex] = 0
                return 0
            if startIndex in memo:
                return memo[startIndex]
            totalWays = dfs(startIndex + 1)
            if startIndex + 1 < len(s) and (s[startIndex] == '1' or  (s[startIndex] == '2' and s[startIndex + 1] <= '6')):
                totalWays += dfs(startIndex + 2)
            memo[startIndex] = totalWays
            return totalWays
        return dfs(0)
