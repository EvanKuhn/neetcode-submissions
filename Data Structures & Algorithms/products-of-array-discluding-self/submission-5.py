# Naive solution:
# - Multiply all the integers together = full_product
# - Divide full_product by the integer at index i to get value at i
# - FAILS if any integer is zero
#
# Aha!
# - Say we create a new array and at index i, we record the value of
#   the product of all integers before (to the left of) i.
# - Likewise, we do the same going from the right (after i).
# - Then to get the answer at index i, we take do:
#      result = left_products[i] * right_products[i]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n

        for i in range(1, n):
            left_products[i] = left_products[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            right_products[i] = right_products[i+1] * nums[i+1]
        
        # print(nums)
        # print(left_products)
        # print(right_products)

        results = [0] * n
        results[0] = right_products[0]
        results[n-1] = left_products[n-1]

        for i in range(1, n-1):
            results[i] = left_products[i] * right_products[i]

        return results

