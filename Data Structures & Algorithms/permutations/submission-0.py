class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        def dfs(start_index, path):
            if start_index == len(nums):
                res.append(path.copy())
                return
            for num in nums:
                if num in visited:
                    continue
                path.append(num)
                visited.add(num)
                dfs(start_index + 1, path)
                path.pop()
                visited.remove(num)
        dfs(0, [])
        return res

            