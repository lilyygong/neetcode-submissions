from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def concat_nums(a, b):
            if(str(a) + str(b) < str(b) + str(a)):
                return 1
            else:
                return -1
        sorted_list = sorted(nums, key = cmp_to_key(concat_nums))
        output = ''.join(str(num) for num in sorted_list)
        if output[0] == '0':
            return '0'
        return output