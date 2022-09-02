class Solution:
    def countVowelPermutation(self, n: int) -> int:
        perms = {'a' : 1,
                 'e' : 1,
                 'i' : 1,
                 'o' : 1,
                 'u' :1 }
        
        for cur in range(1, n):
            temp = perms.copy()
            perms['a'] = (temp['e'] + temp['i'] + temp['u']) %  (10 ** 9 + 7)
            perms['e'] = (temp['i'] + temp['a']) % (10 ** 9 + 7)
            perms['i'] = (temp['e'] + temp['o']) % (10 ** 9 + 7)
            perms['o'] = temp['i'] % (10 ** 9 + 7)
            perms['u'] = (temp['i'] + temp['o']) % (10 ** 9 + 7)
            
        
        return sum(perms.values()) % (10 ** 9 + 7)    
