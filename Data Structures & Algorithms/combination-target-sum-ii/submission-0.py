class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []
        def dfs(startIndex, path, remaining):
            if remaining == 0:
                res.append(path.copy())
                return
            if remaining < 0:
                return
            for i in range(startIndex, len(candidates)):
                if i > 0 and i > startIndex and candidates[i] == candidates[i - 1]: # skip duplicates   
                    continue

                path.append(candidates[i])
                dfs(i + 1, path, remaining - candidates[i]) 
                path.pop()
        dfs(0, [], target)
        return res