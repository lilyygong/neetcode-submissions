class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search - at the pivot, check if its > than
        # the left half, then search the right half
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]: # if nums is alr sorted
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res