class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(startIndex, path):
            if startIndex == len(nums):
                res.append(path.copy())
                return
            path.append(nums[startIndex])
            dfs(startIndex + 1, path)
            path.pop()
            while startIndex + 1 < len(nums) and nums[startIndex] == nums[startIndex + 1]:
                startIndex += 1
            dfs(startIndex + 1, path)
        dfs(0, [])
        return res