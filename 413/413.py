class Solution:
     def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count = 0
        out = 0
        for i in range(1,len(nums)-1):
            if nums[i+1]-nums[i]==nums[i]-nums[i-1]:
                count+=1
            else:
                count=0
            out+=count              
        return out
            
        
