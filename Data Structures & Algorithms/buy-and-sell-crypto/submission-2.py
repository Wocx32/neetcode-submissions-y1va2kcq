class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minBuy = prices[0]
        maxP = 0

        for price in prices:
            maxP = max(maxP, price - minBuy)

            if price < minBuy:
                minBuy = price
        
        return maxP