class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []


        def backtrack(curr, added):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            

            for i in range(len(nums)):
                if not added[i]:
                    curr.append(nums[i])
                    added[i] = True
                    backtrack(curr, added)
                    curr.pop()
                    added[i] = False
        
        backtrack([], [False] * len(nums))
        return res