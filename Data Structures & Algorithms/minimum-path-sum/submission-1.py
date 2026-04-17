class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        dp = {}
        
        def dfs(r, c):
            
            if r + 1 == len(grid) and c + 1 == len(grid[0]):
                return grid[r][c]

            if r >= len(grid) or c >= len(grid[0]):
                return float('inf')
            
            if (r, c) in dp:
                return dp[(r, c)]
            
            dp[(r, c)] = grid[r][c] + min(dfs(r + 1, c), dfs(r, c + 1))
            return dp[(r, c)]

        return dfs(0, 0)