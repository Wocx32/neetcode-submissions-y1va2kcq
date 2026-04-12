class Solution:
    def countSubstrings(self, s: str) -> int:
        
        cache = {}

        def dfs(i, j):
            if i >= j:
                return True
            
            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == s[j]:
                cache[(i, j)] = dfs(i + 1, j - 1)
                return cache[(i, j)]    
        
            cache[(i, j)] = False
            return cache[(i, j)]
        
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                res += dfs(i, j)
    

        return res