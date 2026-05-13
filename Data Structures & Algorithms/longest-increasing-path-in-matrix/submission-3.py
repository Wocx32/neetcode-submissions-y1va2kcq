class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r, c, prev):

            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                prev >= matrix[r][c]
            ):
                return 0

            if (r, c) in dp:
                return dp[(r, c)]
            
            curr = matrix[r][c]

            dp[(r, c)] = 1 + max(
                dfs(r + 1, c, curr),
                dfs(r - 1, c, curr),
                dfs(r, c + 1, curr),
                dfs(r, c - 1, curr),
            )

            return dp[(r, c)]

        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c, -1))
        
        return res