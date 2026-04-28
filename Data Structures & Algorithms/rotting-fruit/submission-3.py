class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()

        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
        
                if grid[r][c] == 1:
                    fresh += 1
        
        def rot(r, c):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                grid[r][c] != 1
            ):
                return False
            
            grid[r][c] = 2
            return True

        minute = 0

        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    if rot(r + dr, c + dc):
                        q.append((r + dr, c + dc))
                        fresh -= 1     
            minute += 1
        
        if fresh == 0:
            return minute
        return -1

                