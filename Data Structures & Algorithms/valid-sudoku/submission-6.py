class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for row in range(9):
            for col in range(9):

                val = board[row][col]
                square = (row // 3) * 3 + (col // 3)

                if val == ".":
                    continue

                mask = 1 << (int(val))

                if rows[row] & mask or cols[col] & mask or squares[square] & mask:
                    return False
                
                rows[row] |= mask
                cols[col] |= mask
                squares[square] |= mask
        
        return True