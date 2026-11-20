class Solution:

    def increasing(self, nums: List[int], i: int, m: int) -> bool:
        assert i < m, f"increasing() given i={i}, m={m}"
        if i == m-1:
            return True
        return nums[i] < nums[m-1]


    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        # Edge cases:
        # Single element array
        if n == 1:
            return nums[0]
        # 2-element array
        if n == 2:
            return min(nums)
        # Unsorted array
        if nums[0] < nums[n-1]:
            return nums[0]

        # Thinking:
        # - Split the array into two equal parts
        # - If both subarrays are strictly increasing, take the smaller
        #   starting value of the two
        # - If one sub-array is strictly increasing, ignore it
        # - The other sub-array has the rotation

        i = 0
        j = n

        while True:
            curlen = j - i
            
            # # Stopping points
            # if curlen == 1:
            #     return nums[i]
            # if curlen == 2:
            #     return min(nums[i:j])

            # Pick midpoint
            m = i + (curlen // 2)

            # We now have two range: [i:m], [m:j]
            #print(f"part1={nums[i:m]}  part2={nums[m:j]}")

            # If both parts are increasing, then pick the smallest 
            # beginning number of the two
            left_incr = self.increasing(nums, i, m)
            right_incr = self.increasing(nums, m, j)
            #print(f"- left_incr={left_incr}, right_incr={right_incr}")

            if left_incr and right_incr:
                return min(nums[i], nums[m])

            if left_incr:
                i = m
            else:
                j = m

        return -1  # TODO


