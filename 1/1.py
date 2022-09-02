class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = 0
        for i in range(len(nums)):
            temp = target - nums[i]
            nums[i] = ''
            if temp in nums[i+1:len(nums)]:
                return[i,nums.index(temp)]
