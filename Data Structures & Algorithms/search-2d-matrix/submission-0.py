class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lenRows = len(matrix)
        lenCols = len(matrix[0])
        n = lenRows * lenCols

        def search(matrix, l, r, target):
            if l > r:
                return False
            
            mid = l + (r - l) // 2

            row = mid // lenCols
            col = mid % lenCols

            val = matrix[row][col]

            if val == target:
                return True
            
            if target < val:
                return search(matrix, l, mid - 1, target)
            
            return search(matrix, mid + 1, r, target)
        
        return search(matrix, 0, n - 1, target)
