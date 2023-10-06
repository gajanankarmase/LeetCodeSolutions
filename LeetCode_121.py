class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = prices[0]
        max_profit = 0

        for i in prices:
            if i < min_price:
                min_price = i
            else:
                max_profit = max(max_profit, i - min_price)
        return max_profit
