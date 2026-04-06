class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        

        for row in range(9):
            for col in range(9):

                val = board[row][col]
                square = (row // 3) * 3 + (col // 3)

                if val == ".":
                    continue
                if val in rows[row] or val in cols[col] or val in squares[square]:
                    return False
                
                rows[row].add(val)
                cols[col].add(val)
                squares[square].add(val)
        
        return True