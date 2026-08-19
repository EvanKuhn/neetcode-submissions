from collections import defaultdict

class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Approach:
        # - First, sort numbers
        # - Then we maintain three pointers (i,j,k), with j being the 'current'
        #   number. Index i will move to the left, and k to the right. We'll move 
        #   these left and right as needed.
        # - Stop when... ???
        nums.sort()
        #for j, b in enumerate(nums):
        return []



class Solution:
    # O(n^2) running time. Too slow.
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
        nums.sort()
        new_nums = []
        cur_value = None
        cur_count = 0
        for n in nums:
            if n != cur_value:
                new_nums.append(n)
                cur_value = n
                cur_count = 1
            elif n == 0 and cur_count < 3:
                new_nums.append(n)
                cur_count += 1
            elif cur_count < 2:
                new_nums.append(n)
                cur_count += 1

        
        print(f"nums = {nums}")
        print(f"new_nums = {new_nums}")
        nums = new_nums

        print(new_nums)

        # Get map of value to numbers that sum to it
        sum_to_pairs_map = self.get_sum_to_pairs_map(nums)
        #print(sum_to_pairs_map)

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
         



