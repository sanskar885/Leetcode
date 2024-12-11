class Solution(object):
    def removeElement(self, nums, val):
        pos=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[pos]= nums[i]
                pos = pos+1
        return pos

        