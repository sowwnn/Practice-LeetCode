class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        import numpy as np
        res = np.rot90(np.array(matrix),3).tolist()
        matrix.clear()
        matrix.extend(res)
        
