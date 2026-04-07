class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for c in s:
            if c not in mapping:
                stack.append(c)
            elif stack and stack[-1] == mapping[c]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0