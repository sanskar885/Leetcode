class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        out=[]
        for x in nums:
            count=0
            for y in nums:
                if x>y:
                    count+=1
            out.append(count)
        return out

       
        