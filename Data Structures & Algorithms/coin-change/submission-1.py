
Result = namedtuple('Result', ['count', 'valid'])

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        mincoin = min(coins)

        if amount == 0:
            return 0


        def count_ways(amount: int) -> Result:
            nonlocal coins, memo

            # Base cases
            if amount in coins:
                return Result(1, True)
            if amount < mincoin:
                return Result(0, False)

            if amount not in memo:
                # Make recursive calls for each possible coin
                # that we can select.
                results = [
                    count_ways(amount-coin) 
                    for coin in coins
                    if coin <= amount
                ]
                # print(f"{amount}: results={results}")

                # Add 1 to each valid result count
                counts = [1 + r.count for r in results if r.valid]
                # print(f"{amount}: counts={counts}")

                # Determine the final Result object (count and
                # validity), and save it.
                if counts:
                    r = Result(min(counts), True)
                else:
                    r = Result(0, False)
                memo[amount] = r

            return memo[amount]

        r = count_ways(amount)
        return r.count if r.valid else -1
            
        