class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counts = {}
        max_freq = 0
        left = 0
        result = 0
        for right in range(len(s)):
            char_counts[s[right]] = char_counts.get(s[right], 0) + 1
            max_freq = max(max_freq, char_counts[s[right]])
            while (right - left + 1) - max_freq > k:
                char_counts[s[left]] = char_counts.get(s[left], 0) - 1
                left += 1
            result = max(result, right - left + 1)
        return result


