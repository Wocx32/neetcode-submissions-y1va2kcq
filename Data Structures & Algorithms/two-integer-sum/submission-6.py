class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for idx, i in enumerate(nums):
            if (target - i) in seen:
                return [seen[(target - i)], idx]
            else:
                seen[i] = idx
        
