class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        profit=0
        cheapest_price=prices[0]
        for i in range(0,len(prices)):
            if prices[i] < cheapest_price:
                cheapest_price=prices[i]
            profit=prices[i] - cheapest_price
            if profit > max_profit:
                max_profit=profit
        print(max_profit)
        return max_profit