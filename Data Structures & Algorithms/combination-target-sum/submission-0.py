class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, subset, curr):
            if curr > target:
                return 
            if curr == target:
                res.append(subset.copy())
                return
            if i >= len(nums):
                return
            
            subset.append(nums[i])
            dfs(i, subset, curr + nums[i])
            subset.pop()
            dfs(i + 1, subset, curr)

        
        dfs(0, [], 0)
        return res