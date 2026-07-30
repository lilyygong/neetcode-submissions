class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 2 pointers, shift the one that's less
        # calculate the area and store it as max value
        maxArea = 0 
        l, r = 0, len(heights) - 1
        while l < r:
            currArea = (r - l) * (min(heights[l], heights[r]))
            maxArea = max(maxArea, currArea)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea