class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {}
        
        def dfs(i, total):
            if i >= len(coins) or total > amount:
                return float('inf')
            
            if total == amount:
                return 0
            
            if (i, total) in dp:
                return dp[(i, total)]


            dp[(i, total)] = min(1 + dfs(i, total + coins[i]), dfs(i + 1, total))
            return dp[(i, total)]
        
        res = dfs(0, 0)

        return res if res != float('inf') else -1