class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        dp = {}
        
        def dfs(i, j):
            if i == j:
                return 1
            
            if i > j:
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]    

            if s[i] == s[j]:
                dp[(i, j)] = 2 + dfs(i + 1, j - 1)
            else:
                dp[(i, j)] = max(dfs(i + 1, j), dfs(i, j - 1))

            return dp[(i, j)]

        return dfs(0, len(s) - 1)