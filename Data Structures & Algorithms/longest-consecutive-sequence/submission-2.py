class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # Put all numbers in a hash set. Use to test if a number exists.
        numset = set(nums)

        # Pick a number. Go left and right and see how big of a range
        # we can construct. Remove numbers as you go.
        lower = 0
        upper = 0

        while numset:
            n = numset.pop()
            l = n
            r = n

            while numset and l-1 in numset:
                l -= 1
                numset.remove(l)

            while numset and r+1 in numset:
                r += 1
                numset.remove(r)

            if r-l > upper - lower:
                lower = l
                upper = r
            
        return upper - lower + 1
