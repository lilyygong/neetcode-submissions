class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # get size of window, is it less than k
        l = 0
        res = 0
        count = {}
        for r in range(len(s)): # rptr going thru every char in s
            count[s[r]] = 1 + count.get(s[r], 0)
            while(r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


