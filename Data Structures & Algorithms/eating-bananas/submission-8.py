import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        curr_hours = 0
        poss_min = 0
        if len(piles) == 1:
            return math.ceil(piles[0] / h)
        left, right = 1, max(piles)
        while left <= right:
            curr_hours = 0
            middle = (left + right) // 2
            for pile in piles:
                curr_hours += math.ceil(pile / middle)
            if curr_hours > h:
                left = middle + 1
            else:
                poss_min = middle
                right = middle - 1
        return poss_min
        
