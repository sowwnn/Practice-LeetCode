class Solution:
    def divide(self,p,q):
        if(p%2 ==0) & (q%2==0):
            return self.divide(p//2,q//2)
        else:
            return p,q
    def mirrorReflection(self, p: int, q: int) -> int:
        p,q = self.divide(p,q)
        
        if (q%2)!=0 :
            if (p%2)==0 :
                return 2
            else: return 1
        else: return 0  
