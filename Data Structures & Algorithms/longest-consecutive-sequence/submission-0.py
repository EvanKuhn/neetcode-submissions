class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Add numbers to a set
        uniqs = set(nums)
        max_len = 0

        # For each number, see how long of a set we can construct 
        while len(uniqs) > 0:
            # Get the first element. This runs in O(1)
            n = next(iter(uniqs))

            # Move left and right (lower and higher)
            l, r = n, n
            while l-1 in uniqs:
                l = l-1
            while r+1 in uniqs:
                r = r+1
            
            # l and r now define the min and max of the sequence
            cur_len = (r - l) + 1
            if cur_len > max_len:
                max_len = cur_len

            # Now remove all of those numbers from the set
            for x in range(l, r+1):
                uniqs.remove(x)

        return max_len