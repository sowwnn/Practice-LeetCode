class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return True if(n > 0 and log(n,4).is_integer()) else False
