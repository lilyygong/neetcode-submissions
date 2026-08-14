class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write = 0
        for read in range(len(nums)):
            if len(nums) == 1:
                break
            print(write, read)
            if nums[read] != 0:
                temp = nums[write]
                nums[write] = nums[read]
                nums[read] = temp
                write += 1
