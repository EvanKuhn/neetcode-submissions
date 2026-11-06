# Iterative solution
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        results = [0] * (n+1)  # Min cost to get TO step i

        for i in range(2, n+1):
            cost1 = results[i-1] + cost[i-1]
            cost2 = results[i-2] + cost[i-2]
            results[i] = min(cost1, cost2)

        return results[n]
        