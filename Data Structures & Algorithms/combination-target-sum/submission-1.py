class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(i, curr, currTotal):
            if currTotal == target:
                res.append(curr.copy())
                return
            
            if currTotal > target:
                return
            
            if i >= len(nums):
                return
            

            curr.append(nums[i])
            dfs(i, curr, currTotal + nums[i])
            curr.pop()
            dfs(i + 1, curr, currTotal)
        
        dfs(0, [], 0)

        return res