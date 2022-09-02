class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        prob = log(buckets) / log(minutesToTest / minutesToDie + 1)
        res = ceil(prob)
        return res
