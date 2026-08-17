class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write, read = 0, 0
        for i in range(len(nums)):
            if nums[read] != 0:
                temp = nums[write]
                nums[write] = nums[read]
                nums[read] = temp
                write += 1
                read += 1
            else:
                read += 1
