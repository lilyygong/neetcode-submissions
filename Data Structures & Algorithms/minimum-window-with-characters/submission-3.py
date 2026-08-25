from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_hash = {}
        curr_window = {}
        min_substring = []
        left = 0
        output = ""
        best_len = float("inf")
        best_left, best_right = 0, 0
        if len(t) > len(s):
            return ""
        for c in t:
            t_hash[c] = t_hash.get(c, 0) + 1
        need = len(t_hash)
        have = 0
        for right in range(len(s)):
            curr_window[s[right]] = curr_window.get(s[right], 0) + 1
            if s[right] in t_hash and curr_window[s[right]] == t_hash[s[right]]:
                have += 1
            while need == have:
                if (right - left + 1) < best_len:
                    best_left, best_right = left, right
                    best_len = right - left + 1
                curr_window[s[left]] = curr_window.get(s[left], 0) - 1
                if s[left] in t_hash and curr_window[s[left]] < t_hash[s[left]]:
                    have -= 1
                left += 1
        if best_len == float("inf"):
            return ""
        output = s[best_left:best_right + 1]
        return output

            
