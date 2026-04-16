class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        part = []

        def dfs(i, curSum):

            if curSum == target:
                res.append(part.copy())
                return

            if curSum > target:
                return

            if i >= len(nums):
                return
            

            for j in range(i, len(nums)):
                part.append(nums[j])
                dfs(j, curSum + nums[j])
                part.pop()

        dfs(0, 0)
        return res