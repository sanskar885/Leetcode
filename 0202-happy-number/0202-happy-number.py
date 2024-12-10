class Solution(object):
    def isHappy(self, n):
        def sqsum(num):
            result = 0
            while num > 0:
                r = num % 10
                result += r * r
                num //= 10
            return result

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sqsum(n)
        
        return n == 1
