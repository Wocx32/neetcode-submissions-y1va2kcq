class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        dp = {}

        def dfs(r, c):
            if r == m - 1 and c == n - 1:
                return grid[r][c]
            if r == m or c == n:
                return float('inf')
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            dp[(r, c)] = grid[r][c] + min(dfs(r + 1, c), dfs(r, c + 1))
            return dp[(r, c)]

        return dfs(0, 0)