class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        dp = [False] * len(nums)
        dp[len(nums) - 1] = True
    
        for i in range(len(nums) - 2, -1, -1):
            end = min(len(nums) - 1, i + nums[i])

            for j in range(i + 1, end + 1):
                if dp[j]:
                    dp[i] = True
                    break
            
        return dp[0]