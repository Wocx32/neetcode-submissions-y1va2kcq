class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        dp = {}

        def dfs(i, remaining):
            if (i, remaining) in dp:
                return dp[(i, remaining)]
                
            if remaining == 0:
                return True
            
            if i >= len(nums) or remaining < 0:
                dp[(i, remaining)] = False
                return False
            

            dp[(i, remaining)] = dfs(i + 1, remaining) or dfs(i + 1, remaining - nums[i])
            return dp[(i, remaining)]

        return dfs(0, sum(nums) / 2)