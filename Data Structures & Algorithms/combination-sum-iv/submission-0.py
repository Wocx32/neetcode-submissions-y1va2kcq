class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = {}

        def dfs(remaining):
            if remaining == 0:
                return 1
            
            if remaining < 0:
                return 0
            
            if remaining in dp:
                return dp[remaining]

            res = 0
            for num in nums:
                res += dfs(remaining - num)

            dp[remaining] = res
            return res

        return dfs(target)