class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                target = [nums[i], nums[left], nums[right]]
                if nums[left] + nums[right] + nums[i] == 0 and target not in result:
                    result.append(target)
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                else:
                    right -= 1
        return result