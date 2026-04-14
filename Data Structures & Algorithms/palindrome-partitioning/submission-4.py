class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        part = []

        def dfs(i):
            if i == len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if isPali(i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()

        dp = {}

        def isPali(i, j):
            if (i, j) not in dp:
                dp[(i, j)] = s[i : j + 1] == s[i : j + 1][::-1]
            
            return dp[(i, j)]

        dfs(0)
        return res