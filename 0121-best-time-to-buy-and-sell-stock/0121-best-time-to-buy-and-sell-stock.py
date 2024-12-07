class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price=float('inf')
        max_prof=0
        for price in prices:
            min_price=min(min_price,price)
            max_prof=max(max_prof,price-min_price   )
        return max_prof
