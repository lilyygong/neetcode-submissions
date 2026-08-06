class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left, right = 1, piles[-1]
        curr_min = 0
        while left <= right:
            curr_rate = 0
            middle = (left + right) // 2
            for i in range(0, (len(piles))):
                curr_rate += math.ceil(piles[i] / middle)
            if curr_rate <= h:
                curr_min = middle
                right = middle - 1
            else:
                left = middle + 1
        return curr_min