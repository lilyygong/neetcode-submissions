class Solution:
    def isPalindrome(self, s: str) -> bool:
        # need to convert to lowercase, no spaces
        # [::-1] for the backwards of a string
        res = ""
        for c in s:
            if c.isalnum():
                res += c.lower()
        return res == res[::-1]