class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        totalSum = nums[0]
        currSum = 0

        for i in nums:
            if currSum < 0:
                currSum = 0
            
            currSum += i
            totalSum = max(totalSum, currSum)
        
        return totalSum