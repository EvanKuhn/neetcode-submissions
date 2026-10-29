class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0  # Purchase price index
        r = 1  # Sale price index
        n = len(prices)
        max_profit = 0

        while r < n:
            if prices[r] < prices[l]:
                # We found a lower purchase price! 
                l = r
            else:
                # See if we found a better sale price
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            
            # Check the next day's price
            r += 1

        return max_profit



        