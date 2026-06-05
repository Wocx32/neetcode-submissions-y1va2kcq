class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}

        def dfs(i, target):
            if i == len(nums):
                return target == 0
            
            if (i, target) in dp:
                return dp[(i, target)]

            res = dfs(i + 1, target + nums[i]) + dfs(i + 1, target - nums[i])

            dp[(i, target)] = res
            return res
        
        return dfs(0, target)
        