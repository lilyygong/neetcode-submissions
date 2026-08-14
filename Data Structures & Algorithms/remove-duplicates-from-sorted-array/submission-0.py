class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write, read = 0, 1
        if len(nums) == 1:
            return 1
        while read < len(nums):
            if nums[read] == nums[write]:
                del nums[read]
            else:
                read += 1
                write += 1
            print(write, read)
        return len(nums)