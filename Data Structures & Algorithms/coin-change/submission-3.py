class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(remaining):
            if remaining == 0:
                memo[remaining] = 0
                return 0
            if remaining in memo:
                return memo[remaining]
            res = float('inf')
            for coin in coins:
                if remaining >= 0:
                    res = min(res, 1 + dfs(remaining - coin))
            memo[remaining] = res
            return res
        temp = dfs(amount)
        return -1 if temp == float('inf') else temp
        