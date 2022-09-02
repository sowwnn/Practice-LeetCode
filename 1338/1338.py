from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        half = len(arr)//2

        arr = list(Counter(arr).values())
        arr.sort(reverse=True)
        ans = 0
        while half > 0:
            half -= arr[ans]
            ans += 1
        return ans
