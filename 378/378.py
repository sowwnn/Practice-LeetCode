import numpy as np

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = np.array(matrix).flatten()
        arr.sort(kind=('heapsort'))
        return arr[k-1]
