class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = [[]]

        # Generate all possible results
        for x in nums:
            results = results + [r + [x] for r in results]

        # Put into a set to get rid of duplicates
        tuples = [tuple(sorted(r)) for r in results]
        uniqs = set(tuples)
        return [list(x) for x in uniqs]