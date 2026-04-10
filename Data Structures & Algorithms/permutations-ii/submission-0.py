class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = set()

        def backtrack(curr, added):
            if len(curr) == len(nums):
                res.add(tuple(curr))
                return
            
            for i in range(len(nums)):
                if not added[i]:
                    curr.append(nums[i])
                    added[i] = True

                    backtrack(curr, added)

                    curr.pop()
                    added[i] = False
        
        backtrack([], [False] * len(nums))
        return [list(i) for i in res]