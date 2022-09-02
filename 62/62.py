# import numpy as np
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        out = math.factorial(m+n-2) // math.factorial(n-1) // math.factorial(m-1)
        return out
