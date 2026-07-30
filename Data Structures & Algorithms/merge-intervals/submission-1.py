class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            last_merged = result[-1]
            curr = intervals[i]
            if last_merged[1] >= curr[0]:
                last_merged[1] = max(last_merged[1], curr[1])
            else:
                result.append(curr)
        return result
