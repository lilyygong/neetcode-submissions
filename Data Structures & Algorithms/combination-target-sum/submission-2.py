class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(startIndex, path, remaining):
            if remaining == 0:
                res.append(path.copy())
                return
            if remaining < 0:
                return
            for i in range(startIndex, len(nums)):
                path.append(nums[i])
                dfs(i, path, remaining - nums[i])
                path.pop()
            startIndex += 1
        dfs(0, [], target)
        return res