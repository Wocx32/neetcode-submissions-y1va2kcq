class Solution:
    def jump(self, nums: List[int]) -> int:
        
        dp = [len(nums)] * len(nums)
    
        dp[len(nums) - 1] = 0
    
        for i in range(len(nums) - 2, -1, -1):

            end = min(len(nums), i + nums[i] + 1)
            for j in range(i + 1, end):
                dp[i] = min(dp[i], 1 + dp[j])
        
        return dp[0]