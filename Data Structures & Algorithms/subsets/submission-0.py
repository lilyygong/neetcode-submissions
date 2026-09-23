class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(start_index, path):
            if start_index == len(nums):
                res.append(path.copy())
                return
            #include the number
            path.append(nums[start_index])
            dfs(start_index + 1, path)
            path.pop()
            dfs(start_index + 1, path)
        dfs(0, [])
        return res