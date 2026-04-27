class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2:
            return False
        
        dp = {}

        def dfs(i, target):
            if target == 0:
                return True
            
            if i >= len(nums) or target < 0:
                return False

            if (i, target) in dp:
                return dp[(i, target)]

            dp[(i, target)] = dfs(i + 1, target - nums[i]) or dfs(i + 1, target)
            return dp[(i, target)]

        return dfs(0, sum(nums) // 2)