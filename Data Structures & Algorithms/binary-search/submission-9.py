class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if not nums:
        #     return -1
        # if len(nums) == 1:
        #     return 0 if nums[0] == target else -1
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            # Compute middle index
            m = l + ((r - l) // 2)

            # Go right or left
            # - Ensure that l and r change by at least 1
            if target < nums[m]:
                r = min(m, r-1)
            elif target > nums[m]:
                l = max(m, l+1)
            else:
                return m

        return -1