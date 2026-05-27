class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def backtrack(idx, curr):
            if idx == len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[idx])
            backtrack(idx + 1, curr)
            curr.pop()
            backtrack(idx + 1, curr)

        backtrack(0, [])
        return res