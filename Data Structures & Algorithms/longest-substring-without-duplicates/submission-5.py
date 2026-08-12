class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 1
        curr_max, total_max = 1, 1
        curr_window = {}
        if len(s) == 0 or len(s) == 1:
            return len(s)
        curr_window[s[left]] = curr_window.get(s[left], 0) + 1
        while right <= len(s) - 1:
            curr_window[s[right]] = curr_window.get(s[right], 0) + 1
            curr_max += 1
            while curr_window.get(s[right], 0) > 1:
                curr_window[s[left]] -= 1
                left += 1
                curr_max -= 1
            right += 1
            if curr_max > total_max:
                total_max = curr_max
        return total_max