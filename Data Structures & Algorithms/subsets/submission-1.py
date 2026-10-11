class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(startIndex, path):
            if startIndex >= len(nums):
                res.append(path.copy())
                return
            path.append(nums[startIndex])
            dfs(startIndex + 1, path)
            path.pop()
            dfs(startIndex + 1, path)
        dfs(0, [])
        return res