class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod, zero_cnt = 1, 0
        for i in nums:
            if i == 0:
                zero_cnt += 1
            else:
                prod *= i
        
        if zero_cnt > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)
        for idx, i in enumerate(nums):
            if zero_cnt > 0:
                if i == 0:
                    res[idx] = prod
                    return res
            else:
                res[idx] = prod // i
        
        return res
