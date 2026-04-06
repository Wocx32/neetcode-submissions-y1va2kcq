class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range(9):
            seen = set()

            for i in range(9):
                if board[row][i] == ".":
                    continue
                elif board[row][i] in seen:
                    return False
                else:
                    seen.add(board[row][i])
        
        for col in range(9):
            seen = set()

            for i in range(9):
                
                if board[i][col] == ".":
                    continue
                
                elif board[i][col] in seen:
                    return False
                
                else:
                    seen.add(board[i][col])
        
        for s in range(9):
            seen = set()

            for i in range(3):
                for j in range(3):
                    row = (s // 3) * 3 + i
                    col = (s % 3) * 3 + j

                    if board[row][col] == ".":
                        continue
                    elif board[row][col] in seen:
                        return False
                    else:
                        seen.add(board[row][col])

        return True

