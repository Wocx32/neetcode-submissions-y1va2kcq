class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        count = defaultdict(int)
        A = []
        
        for i in candidates:
            if count[i] == 0:
                A.append(i)
            count[i] += 1
        


        def dfs(i, currList, total):
            if total == target:
                res.append(currList.copy())
                return
            
            if i >= len(A) or total > target:
                return 

            if count[A[i]] > 0:
                currList.append(A[i])
                count[A[i]] -= 1
                dfs(i, currList, total + A[i])
                count[A[i]] += 1
                currList.pop()
            dfs(i + 1, currList, total)
        
        dfs(0, [], 0)
        return res