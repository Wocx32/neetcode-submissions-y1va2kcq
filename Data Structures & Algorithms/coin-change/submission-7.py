class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {}

        def dfs(i, remaining):
            if remaining == 0:
                return 0
            
            if i >= len(coins) or remaining < 0:
                return float('inf')
            
            if (i, remaining) in dp:
                return dp[(i, remaining)]

            dp[(i, remaining)] = min(1 + dfs(i, remaining - coins[i]), dfs(i + 1, remaining))
            return dp[(i, remaining)]

        res = dfs(0, amount)
        if res == float('inf'):
            return -1
        
        return res