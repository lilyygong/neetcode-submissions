class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        boundary = -1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] >= target:
                right = middle - 1
                boundary = middle
            else:
                left = middle + 1
        return boundary if boundary != -1 else len(nums)
            