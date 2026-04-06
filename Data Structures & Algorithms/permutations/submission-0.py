class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(perm, nums, mask):
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            
            for i in range(len(nums)):
                if not (mask & (1 << i)):
                    perm.append(nums[i])
                    backtrack(perm, nums, mask | (1 << i))
                    perm.pop()
            
        backtrack([], nums, 0)
        return res
