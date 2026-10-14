class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visited = {i: 0 for i in nums}
        for num in nums:
            visited[num] += 1
        res = []
        def dfs(startIndex, path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for n in visited:
                if visited[n] > 0:
                    path.append(n)
                    visited[n] -= 1
                    dfs(startIndex + 1, path)
                    visited[n] += 1
                    path.pop()
        dfs(0, [])
        return res