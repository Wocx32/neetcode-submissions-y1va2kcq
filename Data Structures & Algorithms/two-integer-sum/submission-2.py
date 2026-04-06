class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, i in enumerate(nums):
            required = target - i

            if seen.get(required) != None:

                idx_2 = seen[required]

                return [min(idx, idx_2), max(idx, idx_2)]
            
            else:
                seen[i] = idx
        
