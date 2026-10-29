class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        highest_in_future = prices.copy()
        lowest_in_past = prices.copy()

        for i in range(1, n):
            lowest_in_past[i] = min(lowest_in_past[i-1], prices[i])
        
        for i in range(n-2, -1, -1):
            highest_in_future[i] = max(highest_in_future[i+1], prices[i])

        for i in range(0, n-1):
            profit = max(0, highest_in_future[i+1] - lowest_in_past[i])
            if profit > max_profit:
                max_profit = profit

        return max_profit