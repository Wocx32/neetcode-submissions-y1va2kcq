class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for row in range(9):
            for col in range(9):

                if board[row][col] == ".":
                    continue
                
                val = int(board[row][col]) - 1
                
                if (1 << val) & rows[row]:
                    return False
                if (1 << val) & cols[col]:
                    return False
                if (1 << val) & squares[(row // 3) * 3 + (col // 3)]:
                    return False

                rows[row] |= (1 << val)
                cols[col] |= (1 << val)
                squares[(row // 3) * 3 + (col // 3)] |= (1 << val)

        return True