class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for idx, num in enumerate(nums):
            req = target - num

            if seen.get(req) != None:
                return [seen[req], idx]
            
            seen[num] = idx
        
        print(seen)

        return []