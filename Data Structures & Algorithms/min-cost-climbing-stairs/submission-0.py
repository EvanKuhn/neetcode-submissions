class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        # Thoughts
        # - Base case: cost to reach step 0 or 1 is zero
        # - Cost to reach step i = min(mincost(i-1), mincost(i+1))
        
        def mincost(i: int) -> int:
            nonlocal cost, memo

            # Base case: no cost to step _to_ the first two steps.
            # These are treated as starting points.
            if i < 2:
                return 0

            if i not in memo:
                cost1 = mincost(i-1) + cost[i-1]
                cost2 = mincost(i-2) + cost[i-2]
                memo[i] = min(cost1, cost2)
            return memo[i]

        return mincost(len(cost))