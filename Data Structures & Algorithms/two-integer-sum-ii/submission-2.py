class Solution:
    @staticmethod
    def find_target_in_slice(
        numbers: List[int], i: int, j: int, target: int
    ) -> int:
        '''
        Given an array of numbers, and a pair of indexes i, j, search
        the array between index range [i,j) for the target integer.
        - Note that the value at index j is NOT included.
        - Return the index if the target is found, or -1 if not.
        '''
        # Sanity check
        if j <= i or i < 0 or j < 0:
            return -1

        # TODO: linear search for now. Better would be binary search.
        for x in range(i,j):
            if numbers[x] == target:
                return x
        return -1


    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        last_a = -1

        # We will operate on two index-value pairs: (i, a) and (j, b)
        for i, a in enumerate(numbers):
            # If we saw 'a' before, skip it
            if a == last_a:
                continue
            last_a = a

            # Find out what other number we need
            remain = target - a

            # Search either to the left or right of the current index
            if remain >= a:
                j = self.find_target_in_slice(numbers, i+1, n, remain)
            else:
                j = self.find_target_in_slice(numbers, 0, i, remain)

            # If we found a valid result, return it
            if j != -1:
                return sorted([i+1, j+1])



        