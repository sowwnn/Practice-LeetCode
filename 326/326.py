class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return True if (n>0 and 3**(round(log(n,3)))==n) else False
    
