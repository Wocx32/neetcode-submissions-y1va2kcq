class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefixMap = { 0: 1 }
        res = currSum = 0

        for num in nums:
            
            currSum += num
            diff = prefixMap.get(currSum - k, 0)
            res += diff

            prefixMap[currSum] = 1 + prefixMap.get(currSum, 0)
        
        return res