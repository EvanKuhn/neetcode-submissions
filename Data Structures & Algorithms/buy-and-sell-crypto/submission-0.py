class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0

        # Compute an array of max future prices at index i
        maxes = [0] * n
        maxes[n-1] = prices[n-1]
        for i in range(n-2, -1, -1):
            maxes[i] = max(maxes[i+1], prices[i])

        # Examine max profit at each index
        for i in range(0, n-1):
            cur_price = prices[i]
            max_future_price = maxes[i+1]
            profit = max_future_price - cur_price
            if profit > max_profit:
                max_profit = profit

        return max_profit




        