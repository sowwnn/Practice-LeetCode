class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
      return any(Counter(str(n)) == Counter(str(1 << d)) for d in range(31))
