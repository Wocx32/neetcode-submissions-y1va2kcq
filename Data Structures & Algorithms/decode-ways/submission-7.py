class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = {}

        def dfs(i):

            if i == len(s):
                return 1
            
            if i > len(s):
                return 0

            if i in dp:
                return dp[i]

            res = 0

            if s[i] != '0':

                res += dfs(i + 1)

                if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                    res += dfs(i + 2)
            
            dp[i] = res
            return res
        
        return dfs(0)