class Solution:
    def firstUniqChar(self, s: str) -> int:
        for idx, char in enumerate(s):
            if s.count(char) == 1: return idx
        return -1
