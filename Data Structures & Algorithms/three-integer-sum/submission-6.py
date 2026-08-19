from collections import defaultdict

class Solution:
    def filter_inputs(self, nums: List[int]) -> List[int]:
        '''
        Given a list of numbers, filter it down to remove unnecessary
        duplicates:
        - Allow up to three 0's
          - because [0,0,0] sums to 0
        - Allow up to two of any other number
          - because [a,a,a] never sums to 0 when a!=0
        '''
        nums = sorted(nums)
        new_nums = []
        cur_value = None
        cur_count = 0
        for n in nums:
            if n != cur_value:
                new_nums.append(n)
                cur_value = n
                cur_count = 1
            elif cur_count < 2 or (n == 0 and cur_count < 3):
                new_nums.append(n)
                cur_count += 1
        return new_nums

    def get_sum_to_pairs_map(self, nums: List[int]) -> defaultdict:
        '''
        Given an array numbers, return a dict of:
            value => list of pairs of index-value pairs ((i,a), (j,b)) 
        such that a + b == value.
        Each pair of values is guaranteed to be from different indexes.
        '''
        results = defaultdict(list)
        n = len(nums)
        for i in range(0, n):
            for j in range(i+1, n):
                a, b = nums[i], nums[j]
                results[a+b].append([(i,a), (j,b)])
        return results

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []

        # Massage inputs:
        # - Allow up to three 0's
        # - Allow up to two of any other number
        nums = self.filter_inputs(nums)

        # Get map of value to numbers that sum to it
        sum_to_pairs_map = self.get_sum_to_pairs_map(nums)

        for k, c in enumerate(nums):
            # Given a value 'c', get all pairs that sum to '-c'
            pairs = sum_to_pairs_map[-c]
            for p in pairs:
                i, a = p[0]
                j, b = p[1]
                if k != i and k != j:
                    #print(f"Adding nums[{i}]={a} + nums[{j}]={b} + nums[{k}]={c}")
                    # Store as tuples so we can add to a set
                    results.append(tuple(sorted([a, b, c])))

        # Remove duplicates, convert tuples to arrays, and return
        uniqs = list(set(results))
        return sorted([list(x) for x in uniqs])
         



