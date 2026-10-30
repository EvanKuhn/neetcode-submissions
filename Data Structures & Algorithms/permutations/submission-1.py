class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]


        results = []

        for i in range(0, len(nums)):
            value = nums[i]
            rest = nums[:i] + nums[i+1:]
            sub_results = self.permute(rest)
            new_results = [[value] + s for s in sub_results]
            results.extend(new_results)

        return results
        