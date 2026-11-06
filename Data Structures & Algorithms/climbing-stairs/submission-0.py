class Solution:
    def climbStairs(self, n: int) -> int:
        results = [1] * (n+1)
        for i in range(2, n+1):
            results[i] = results[i-1] + results[i-2]
        return results[n]
        