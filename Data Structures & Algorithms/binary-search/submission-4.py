class Solution:
    def search(self, nums: List[int], target: int) -> int:

        print(f"nums: {nums}")

        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        l = 0
        r = len(nums) - 1
        iterations = 0

        while l <= r:
            iterations += 1
            print(f"iter {iterations}")

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

            print(f"l,r: [{l},{r}]")

            # Compute middle index
            m = l + ((1 + r - l) // 2)
            print(f"m: {m}")

            # Go right or left
            if target < nums[m]:
                r = min(m, r-1)
                print(f"new r={r}")
            elif target > nums[m]:
                l = max(m, l+1)
                print(f"new l={l}")
            else:
                return m

        return -1