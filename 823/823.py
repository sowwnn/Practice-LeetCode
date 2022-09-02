class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        t = {}
        for a in sorted(arr):
            t[a] = 1 + sum(t[b] * t.get(a/b, 0) for b in arr if b < a)
        return sum(t.values()) % (10**9 + 7)

