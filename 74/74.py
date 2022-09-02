class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def searchMatrix(lo, hi, row):
            if lo > hi: return False
            mid = (lo + hi) // 2
            if row is not None:
                if matrix[row][mid] == target: return True
                if target > matrix[row][mid]: return searchMatrix(mid + 1, hi, row)
                return searchMatrix(lo, mid - 1, row)
            if target < matrix[mid][0]: return searchMatrix(lo, mid - 1, row)
            if target > matrix[mid][-1]: return searchMatrix(mid + 1, hi, row)
            return searchMatrix(0, len(matrix[0]) - 1, mid)
        return searchMatrix(0, len(matrix)-1, None)
        
