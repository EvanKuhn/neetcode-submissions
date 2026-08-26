class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            # Check if target out of bounds
            if target < nums[l]:
                return -1
            if target > nums[r]:
                return -1

            # Check if found at edges
            if target == nums[l]:
                return l
            if target == nums[r]:
                return r

            # Compute middle index
            m = l + ((1 + r - l) // 2)

            # Go right or left
            # - Ensure that l and r change by at least 1
            if target < nums[m]:
                r = min(m, r-1)
            elif target > nums[m]:
                l = max(m, l+1)
            else:
                return m

        return -1