class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # insertion sort
        # outer loop picks next elem
        # inner loop shifts right
        for i in range(len(nums)): 
            current = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > current:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = current
        