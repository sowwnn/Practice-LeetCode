class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        
        for idx in range(len(nums)):
            right -= nums[idx]
            if left == right:
                return idx
            left += nums[idx]
            
        return -1
        # temp = [(sum(nums[:i]) - sum(nums[i+1:]) == 0) for i in range(0,len(nums))]
        # # print(temp)
        # try: return temp.index(1) 
        # except: return -1
