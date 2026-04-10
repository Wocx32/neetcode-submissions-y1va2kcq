class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        def backtrack(i, curr, added):

            if i == len(nums):
                res.append(curr.copy())
                return
            

            curr.append(nums[i])
            added[i] = True

            backtrack(i + 1, curr, added)

            curr.pop()
            added[i] = False

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            backtrack(i + 1, curr, added)
        
        backtrack(0, [], [False] * len(nums))
        return res