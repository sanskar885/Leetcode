class Solution(object):
    def moveZeroes(self, nums):
        prev_idx=0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                hold = nums[prev_idx]
                nums[prev_idx]=nums[i]
                nums[i]=hold
                prev_idx+=1
        