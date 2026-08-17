class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = {}
        curr_window = {}
        left = 0
        if len(s1) > len(s2):
            return False
        for c in s1:
            target[c] = target.get(c, 0) + 1
        for char in range(0, len(s1)):
            curr_window[s2[char]] = curr_window.get(s2[char], 0) + 1
        if curr_window == target:
                return True
        for right in range(len(s1), len(s2)):
            # print(curr_window, target)
            # print(right)
            curr_window[s2[right]] = curr_window.get(s2[right], 0) + 1
            curr_window[s2[left]] = curr_window.get(s2[left], 0 ) - 1
            if curr_window[s2[left]] == 0:
                del curr_window[s2[left]]
            left += 1
            if curr_window == target:
                return True
        return False

        