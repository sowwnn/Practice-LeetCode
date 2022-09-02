class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res, looking_for = 0, defaultdict(int)
        for word in words:
            if looking_for[word]:
                looking_for[word] -= 1
                res += 4
                continue
            looking_for[word[1] + word[0]] += 1
        
        for i in looking_for:
            if i[0] == i[1] and looking_for[i]:
                res += 2
                break
        
        return res
