class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def backtrack(curr, added):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            

            for i in nums:
                if i not in added:
                    curr.append(i)
                    added.append(i)
                    backtrack(curr, added)
                    curr.pop()
                    added.pop()
        
        backtrack([], [])
        return res