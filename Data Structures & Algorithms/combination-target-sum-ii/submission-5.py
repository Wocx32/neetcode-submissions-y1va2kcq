class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []

        def backtrack(idx, curr, currSum):

            if currSum == target:
                res.append(curr.copy())
                return
            
            if currSum > target or idx >= len(candidates):
                return
            
            curr.append(candidates[idx])
            backtrack(idx + 1, curr, currSum + candidates[idx])
            curr.pop()

            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            
            backtrack(idx + 1, curr, currSum)
        
        backtrack(0, [], 0)
        return res