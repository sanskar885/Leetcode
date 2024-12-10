class Solution(object):
    def countBits(self, n):
        ans = [0] * (n + 1) 
        for i in range(1, n + 1):  
            halfpos = i // 2  
            if i % 2 == 1: 
                ans[i] = ans[halfpos] + 1 
            else:  
                ans[i] = ans[halfpos]
        return ans