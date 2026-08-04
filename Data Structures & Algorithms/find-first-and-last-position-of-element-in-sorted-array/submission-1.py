class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        left_index = -1
        right_index = -1
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                left_index = middle
                right = middle - 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                right_index = middle
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return [left_index, right_index]