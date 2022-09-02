class Solution:
    def romanToInt(self, s: str) -> int:
        dct = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
        }

        prev = None
        value = 0
        for i in range(len(s)-1,-1,-1):
            letter = s[i]
            if letter == "I" and prev in ("V","X"):
                value-=dct[letter]
            elif letter == "X" and prev in ("L","C"):
                value-=dct[letter]
            elif letter == "C" and prev in ("D","M"):
                value-=dct[letter]
            else:
                value+=dct[letter]
            prev = letter
        return value
