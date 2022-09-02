class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        for i in range(2-rows, cols-1):
            valid = range(max(0,0-i), min(rows,cols-i))
            # print([mat[j][i+j] for j in valid])
            diag = sorted([mat[j][i+j] for j in valid])
            for k in valid:
                mat[k][i+k] = diag.pop(0)
        return mat
