class Solution:
    def divi(self, i):
        return (i%3==0), (i%5==0)
    
    def check(self, i):
        a,b = self.divi(i)
        # print(a,b)
        if(a & b):
            return "FizzBuzz"
        elif(a):
            return "Fizz"
        elif(b):
            return "Buzz"
        else:
            return f'{i}'
        
    def fizzBuzz(self, n: int) -> List[str]:    
        out = [self.check(i+1) for i in range(n)]
        return out
            
        
        
