class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(startIndex, path, total):
            if total == target:
                res.append(path.copy())
                return
            if total > target:
                return
            for num in range(startIndex, len(nums)):
                path.append(nums[num])
                dfs(startIndex, path, total + nums[num])
                path.pop()
                startIndex += 1
        dfs(0, [], 0)
        return res
