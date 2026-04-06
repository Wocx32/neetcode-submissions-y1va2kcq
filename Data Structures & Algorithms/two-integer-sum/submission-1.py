class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for idx, i in enumerate(nums):
            to_find = target - i

            if seen.get(to_find) != None:
                return [seen[to_find], idx]
            
            else:
                seen[i] = idx
    