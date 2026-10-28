from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Get counts of each number
        num_to_count = defaultdict(int)
        for n in nums:
            num_to_count[n] += 1

        # Create list of length=max_count. Populate it such that 
        # each index is the count, and the values are the numbers 
        # with that count.
        max_count = max(num_to_count.values())
        count_to_nums: List = [None] * (max_count+1)

        for num, count in num_to_count.items():
            if count_to_nums[count] is None:
                count_to_nums[count] = []
            count_to_nums[count].append(num)

        # Pick the top k
        results = []
        for i in range(max_count, -1, -1):
            if count_to_nums[i] is not None:
                values = count_to_nums[i]
                while len(results) < k and values:
                    results.append(values.pop())

        return results
        