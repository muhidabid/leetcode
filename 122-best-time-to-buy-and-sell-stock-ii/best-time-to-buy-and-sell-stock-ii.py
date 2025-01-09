class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        tmp_profit = 0
        i = 0
        while i < len(prices)-1:
            if prices[i+1] - prices[i] > 0:
                tmp_profit += prices[i+1] - prices[i]
            i += 1

        return tmp_profit    