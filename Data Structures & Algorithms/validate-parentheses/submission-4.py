class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for c in s:
            if c not in pairs:
                stack.append(c)
            else:
                if stack and pairs[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0