class Solution:
    # Using division will fail if there are zeroes, since zero will wipe 
    # out any info on what numbers were multiplied together.

    # OPTIMIZATION (from the official solution): below I use separate prefix 
    # and postfix arrays to track the products to the left and right of the
    # current index. Instead, we can use a single array and do two passes:
    # - Left to right, store the cumulative product from elements to the left.
    # - Then right to left, multiply by the cumulative product from elems to the right.

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        #print(f"nums: {nums}")
        
        # PASS 1:
        # Keep an array where the value at index i is the product
        # of all elements to the left, i.e. in range [0,i).
        products_left = [None] * n
        for i in range(0, n):
            if i == 0:
                products_left[i] = 1
            elif i == 1:
                products_left[i] = nums[i-1]
            else:
                products_left[i] = nums[i-1] * products_left[i-1]

        #print(f"products_left: {products_left}")

        # PASS 2:
        # Build same array for rightward products
        products_right = [None] * n
        for i in range(n-1, -1, -1):
            if i == n-1:
                products_right[i] = 1
            elif i == n-2:
                products_right[i] = nums[i+1]
            else:
                products_right[i] = nums[i+1] * products_right[i+1]
                
        #print(f"products_right: {products_right}")

        # PASS 3:
        # Compute results: value at index i = products to left + products to right
        results = [0] * n
        for i in range(0, n):
            if i == 0:
                results[i] = products_right[i]
            elif i == n-1:
                results[i] = products_left[i]
            else:
                results[i] = products_left[i] * products_right[i]

        return results



            

            


        
        