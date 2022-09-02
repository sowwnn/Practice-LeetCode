class Solution:
    def search(self, nums: List[int], target: int) -> int:
        self.target = target
        left,right = 0,len(nums)-1
        return self.bisearch(nums, left,right)
        
    def bisearch(self,nums, left, right):
        if left > right: return -1
        
        mid = (left+right)//2
        if nums[mid]==self.target:
            return mid
        elif nums[left]>nums[mid]:
            if nums[mid]<self.target<=nums[right]:
                left = mid+1
            else:
                right = mid-1
        else:
            if nums[left]<=self.target<nums[mid]:
                right = mid-1
            else:
                left = mid+1
        return self.bisearch(nums, left,right)
                    
        
