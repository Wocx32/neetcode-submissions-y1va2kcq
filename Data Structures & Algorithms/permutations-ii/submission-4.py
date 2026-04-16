class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        visited = [False] * len(nums)
        part = []

        def dfs():
            if len(part) == len(nums):
                res.add(tuple(part))
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
        return list(res)
