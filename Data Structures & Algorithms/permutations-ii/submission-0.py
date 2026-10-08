class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = {n: 0 for n in nums}
        for num in nums:
            count[num] += 1
        def dfs(startIndex, path):
            if startIndex == len(nums):
                res.append(path.copy())
                return
            for num in count:
                if count[num] > 0:
                    path.append(num)
                    count[num] -= 1
                    dfs(startIndex + 1, path)
                    count[num] += 1
                    path.pop()
        dfs(0, [])
        return res

            