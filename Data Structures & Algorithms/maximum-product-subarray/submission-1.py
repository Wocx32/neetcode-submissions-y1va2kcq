class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = curr_min = curr_max = nums[0]

        for num in nums[1:]:
            candidates = (num, curr_min * num, curr_max * num)
            curr_max = max(candidates)
            curr_min = min(candidates)
            res = max(res, curr_max)
        
        return res