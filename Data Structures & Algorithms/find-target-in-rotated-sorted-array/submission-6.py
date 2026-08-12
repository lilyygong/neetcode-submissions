class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        target_index = -1
        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            elif nums[middle] < nums[right]: # right side sorted
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
        return target_index