class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {}
        def dfs(need):
            if need == 0:
                return 0
            
            elif need < 0:
                return float('inf')
            
            if need in dp:
                return dp[need]


            res = float('inf')

            for coin in coins:
                res = min(res, 1 + dfs(need - coin))
            
            dp[need] = res
            return res
        
        res = dfs(amount)
        if res == float('inf'):
            return -1
        return res