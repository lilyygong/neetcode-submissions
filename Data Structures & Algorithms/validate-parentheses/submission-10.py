class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(':')', '[':']', '{':'}' }
        if len(s) == 1:
            return False
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if stack and brackets.get(stack[-1]) == c:
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False
    