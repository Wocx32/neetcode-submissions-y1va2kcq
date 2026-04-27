class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def dfs(cur, visit):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if visit[i]:
                    continue
                
                cur.append(nums[i])
                visit[i] = True

                dfs(cur, visit)

                cur.pop()
                visit[i] = False
        

        dfs([], [False] * len(nums))
        return res