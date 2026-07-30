class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # iterate starting from the back and bubble sort
        # concatenate: if a+b > b+a, a should preceed b
        for i in range(len(nums)):
            for j in range(0, len(nums) - i -1):
                if str(nums[j]) + str(nums[j + 1]) < str(nums[j + 1]) + str(nums[j]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        output = ''.join(str(num) for num in nums)
        if output[0] == '0':
            return '0'
        return output
        