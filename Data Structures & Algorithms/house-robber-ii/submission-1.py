class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = {}

        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
            
            if (i, flag) in dp:
                return dp[(i, flag)]

            dp[(i, flag)] = max(
                dfs(i + 1, flag),
                nums[i] + dfs(i + 2, flag or i == 0)
            )

            return dp[(i, flag)]
        
        return dfs(0, False)