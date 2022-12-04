class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        
        buyDay = 0
        sellDay = 0
        profit = 0
        while sellDay < len(prices):
            if prices[sellDay]-prices[buyDay] > profit: 
                profit = prices[sellDay]-prices[buyDay]
                
            elif prices[sellDay]-prices[buyDay] < 0: 
                buyDay = sellDay
                
            sellDay +=1
                
        return profit

            