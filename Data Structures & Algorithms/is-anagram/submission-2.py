class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       newS = {}
       newT = {} 
       if len(s) != len(t):
            return False
       for i in range(len(s)):
        newS[s[i]] = 1 + newS.get(s[i], 0)
        newT[t[i]] = 1 + newT.get(t[i], 0)
       return newS == newT

# first intuition is to check the length of each string
# use a hash map key: letter, value: count.
# 0 is the default value for a hash map so if the key does not
# exist, then the function will return 0 as the default function


