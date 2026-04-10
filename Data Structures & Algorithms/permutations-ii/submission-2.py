class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        def backtrack(curr, added):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if added[i]:
                    continue
                
                if i and nums[i] == nums[i - 1] and not added[i - 1]:
                    continue

                curr.append(nums[i])
                added[i] = True

                backtrack(curr, added)

                curr.pop()
                added[i] = False
        
        backtrack([], [False] * len(nums))
        return res