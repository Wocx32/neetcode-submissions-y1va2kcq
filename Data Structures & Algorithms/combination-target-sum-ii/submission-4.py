class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def backtrack(i, curr, currTotal):

            if currTotal == target:
                res.append(curr.copy())
                return
            
            if i >= len(candidates) or currTotal > target:
                return
            

            curr.append(candidates[i])
            backtrack(i + 1, curr, currTotal + candidates[i])
            curr.pop()

            while i < (len(candidates) - 1) and candidates[i] == candidates[i + 1]:
                i += 1
                
            backtrack(i + 1, curr, currTotal)

        backtrack(0, [], 0)
        return res