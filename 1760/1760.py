class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
            
        out, h, w= [-1]*len(grid[0]), len(grid), len(grid[0])
        for i in range(w):
            col, row = i, 0
            while row < h:
                curr =grid[row][col]
                if ((w)>col+curr>-1) and curr==grid[row][col+(curr)]:
                    row, col = row+1, col + (curr)
                else:
                    col = -1
                    break
            out[i] = col
        return out
