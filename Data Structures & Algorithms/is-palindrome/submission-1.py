class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversedS = ''
        for c in s:
            if c.isalnum():
                reversedS += c.lower()
                print(reversedS)
        return reversedS[::-1] == reversedS

# initial intuition was correct but i need to write these things out
