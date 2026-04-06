class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        res = 0

        op = ['+', '-', '*', '/']

        for tok in tokens:
            if tok not in op:
                stack.append(int(tok))
            
            else:
                right = stack.pop()
                left = stack.pop()

                if tok == "+":
                    stack.append(left + right)
                elif tok == "-":
                    stack.append(left - right)
                elif tok == "*":
                    stack.append(left * right)
                elif tok == "/":
                    stack.append(int(left / right))
        
        print(stack)
        return stack[-1]