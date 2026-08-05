class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[left] < nums[right]: # array is sorted already
            return nums[left]
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > nums[right]: # left side is sorted, search right
                left = middle + 1
            else: # right side is sorted
                right = middle
        return nums[left]