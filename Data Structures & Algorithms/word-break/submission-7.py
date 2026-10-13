class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        result = False
        memo = {}
        def dfs(startIndex):
            nonlocal result
            if startIndex == len(s):
                return True
            if startIndex in memo:
                return memo[startIndex]
            for word in wordDict:
                if s[startIndex:startIndex+len(word)] == word:
                    result = dfs(startIndex + len(word))
                    if result:
                        memo[startIndex] = True
                    else:
                        memo[startIndex] = False
            return result
        return dfs(0)
