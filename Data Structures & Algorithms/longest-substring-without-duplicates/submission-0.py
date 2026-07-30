class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # ensure substring has no duplicates
        # slide left side window when a dup is reached
        # remove letters from the left until the dup is gone
        # use a set bc elem are unique
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res