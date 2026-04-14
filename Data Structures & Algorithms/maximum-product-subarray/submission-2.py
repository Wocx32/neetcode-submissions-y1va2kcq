class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]
        curr_min = 1
        curr_max = 1

        for num in nums:
            candidates = (num, num * curr_min, num * curr_max)
            curr_min = min(candidates)
            curr_max = max(candidates)
            res = max(res, curr_max)
        
        return res