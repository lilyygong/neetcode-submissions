class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers, intuition is that # greater than the target
        # will be on right. if its too big shift rpointer, too small
        # shift lpointer
        l, r = 0, len(numbers) - 1

        while l < r:
            tempSum = numbers[l] + numbers[r]
            if tempSum == target:
                return [1 + l, 1 + r]
            elif tempSum > target:
                r -= 1
            elif tempSum < target:
                l += 1