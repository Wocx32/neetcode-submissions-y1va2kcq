class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def dfs(i, cur, curTotal):

            if curTotal == target:
                res.append(cur.copy())
                return 
            
            if i >= len(candidates):
                return
            
            if curTotal > target:
                return
            
            cur.append(candidates[i])
            dfs(i + 1, cur, curTotal + candidates[i])
            cur.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            dfs(i + 1, cur, curTotal)
        
        dfs(0, [], 0)

        return res