class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def dfs(openB, closeB, curr):
            if openB == closeB == n:
                res.append(''.join(curr))
                return
            
            if openB < n:
                curr.append('(')
                dfs(openB + 1, closeB, curr)
                curr.pop()
            
            if closeB < openB:
                curr.append(')')
                dfs(openB, closeB + 1, curr)
                curr.pop()
            
        
        dfs(0, 0, [])
        return res