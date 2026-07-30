class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        array = set()
        for num in nums:
            if num in array:
                return True
            else:
                array.add(num)
        return False

# first thought - brute force comparison
# refine- add all the values in nums to a hash map bc 
# a hash map must have all unique elements
# i used a set here because there is no need for a key value pair
# a set does not maintain order but has all unique elements
# key idea here is to recognize that a dict/set has unique elements