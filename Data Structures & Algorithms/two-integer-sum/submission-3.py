class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for idx, i in enumerate(nums):
            if seen.get(target - i) != None:
                return [seen.get(target - i), idx]
            else:
                seen[i] = idx
