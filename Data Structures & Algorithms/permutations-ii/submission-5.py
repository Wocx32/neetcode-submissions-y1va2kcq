class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        visited = [False] * len(nums)
        part = []
        nums.sort()

        def dfs():
            if len(part) == len(nums):
                res.append(part.copy())
                return
            

            for i in range(len(nums)):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue

                visited[i] = True
                part.append(nums[i])
                dfs()
                part.pop()
                visited[i] = False
            
    
        dfs()
        return res
