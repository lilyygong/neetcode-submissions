class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0]
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            prefix.append(prefix_sum)
        for j in range(len(prefix) - 1):
            left_sum = prefix[j]
            right_sum = prefix[-1] - left_sum - nums[j]
            if left_sum == right_sum:
                return j
        return -1