class Solution:
    
    def numberOfSubstrings(self, s: str) -> int:
        a = b = c = -1
        count = 0
        for i in range(len(s)):
            char = s[i]
            if(char == "a"):
                a = i
            elif(char == "b"):
                b = i
            else:
                c = i
            if(a != -1 and b != -1 and c != -1):
                count += min([a, b, c]) + 1
        return count
