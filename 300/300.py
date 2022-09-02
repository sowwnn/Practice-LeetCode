class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        out = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] > out[-1]: out.append(nums[i])
            else: out[bisect_left(out,nums[i])]=nums[i]            
        return len(out)
