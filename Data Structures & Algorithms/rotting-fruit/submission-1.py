class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()
        fresh = 0

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        time = 0
        while fresh > 0 and q:
            length = len(q)
            for _ in range(length):
                r, c = q.popleft()
                
                for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    cell = (r + d[0], c + d[1])
                    if (
                        cell[0] in range(len(grid)) and
                        cell[1] in range(len(grid[0])) and
                        grid[cell[0]][cell[1]] == 1
                    ):
                        grid[cell[0]][cell[1]] = 2
                        q.append(cell)
                        fresh -= 1

            time += 1
        
        return time if fresh == 0 else -1
