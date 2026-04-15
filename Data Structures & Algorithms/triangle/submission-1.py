class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp = {}
        def dfs(r, c):
            if r >= len(triangle):
                return 0
            
            if (r, c) in dp:
                return dp[(r, c)]

            dp[(r, c)] = triangle[r][c] + min(dfs(r + 1, c), dfs(r + 1, c + 1))
            return dp[(r, c)]

        return dfs(0, 0)