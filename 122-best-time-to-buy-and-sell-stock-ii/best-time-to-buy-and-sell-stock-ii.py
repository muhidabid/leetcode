class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        sell = prices[0]
        profit = buy-sell
        tmp_profit = 0
        maxV = max(prices)
        minV = min(prices)
        i = 0
        while i < len(prices)-1:
            if prices[i+1] - prices[i] < 0:
                i += 1 
                continue
            tmp_profit += prices[i+1] - prices[i]
            i += 1
            

        return tmp_profit    

            


        