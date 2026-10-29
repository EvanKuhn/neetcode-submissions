# Idea:
# - Maintain left and right pointers
# - Based on leftmost value, determine what we need for rightmost value
# - Move the right pointer to see if it exists
# - If not, increment the left pointer and repeat
# - This works because the numbers are sorted. We know that as we move 
#   the left point, the left value will increase, and therefore we need 
#   to decrease the right value.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = -1
        r = n-1

        while l < r:
            # Increment left pointer
            l += 1

            # Determine the right number we need
            diff = target - numbers[l]

            # Move the right pointer
            while l < r and numbers[r] > diff:
                r -= 1

            # Check for success
            if numbers[r] == diff:
                return [l+1, r+1]
        
        return []