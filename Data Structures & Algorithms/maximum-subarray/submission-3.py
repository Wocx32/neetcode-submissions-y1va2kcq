class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curMax = 0
        maxSub = nums[0]

        for num in nums:
            if curMax < 0:
                curMax = 0
            
            curMax += num

            maxSub = max(maxSub, curMax)
        
        return maxSub