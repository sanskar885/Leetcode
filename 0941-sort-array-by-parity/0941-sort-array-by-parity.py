class Solution(object):
    def sortArrayByParity(self, nums):
        i,j=0,len(nums)-1
        while i<j:
            if nums[i]%2==1:
                nums[i],nums[j]=nums[j],nums[i]
                j=j-1
            else:
                i=i+1
        return nums

