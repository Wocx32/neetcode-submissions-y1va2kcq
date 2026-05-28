class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(i, curr, currSum):

            if currSum == target:
                res.append(curr.copy())
                return
            
            if currSum > target or i == len(nums):
                return
            
            curr.append(nums[i])
            backtrack(i, curr, currSum + nums[i])
            curr.pop()
            backtrack(i + 1, curr, currSum)

        backtrack(0, [], 0)        

        return res
