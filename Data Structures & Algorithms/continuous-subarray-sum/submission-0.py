class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = [0]
        remainders = {}
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            prefix.append(prefix_sum)
        for j in range(len(prefix)):
            remainder = prefix[j] % k
            if remainder not in remainders:
                remainders[remainder] = j
            else:
                last_seen = remainders.get(remainder, 0)
                if j - last_seen >= 2:
                    return True
        return False

            