class Solution(object):
    def majorityElement(self, nums):
        m = 0       
        count = 0   
        for i in range(len(nums)):
            if count == 0:
                m = nums[i] 
                count = 1     
            elif nums[i] == m: 
                count += 1  
            else:
                count -= 1    
        
        
        count = 0  
        for num in nums:
            if num == m:
                count += 1
        if count > len(nums) // 2:
            return m
        else:
            return None  
