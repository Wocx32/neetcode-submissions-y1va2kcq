class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [0] * len(nums)
        prod = 1

        for i in range(len(nums)):
            res[i] = prod
            prod *= nums[i]
        
        prod = 1

        for i in range(len(nums) -1, -1, -1):
            res[i] *= prod
            prod *= nums[i]
        
        return res