class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visited = {i:0 for i in nums}
        for j in nums:
            visited[j] += 1
        res = []
        def dfs(startIndex, path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for num in visited:
                if visited[num] > 0:
                    path.append(num)
                    visited[num] -= 1
                    dfs(startIndex + 1, path)
                    path.pop()
                    visited[num] += 1
        dfs(0 , [])
        return res
            