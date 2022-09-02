class Solution:
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        arr = []
        while len(matrix) != 0:
            arr += matrix.pop(0)
            matrix = (list(zip(*matrix)))[::-1]
        return arr
        
