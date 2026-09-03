class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        for i in range(0,len(nums)):
            value = nums[i]
            rest = nums[i:]

            if value == target:
                results.append([value])
            elif value < target:
                sub_results = self.combinationSum(rest, target-value)
                new_results = [[value] + s for s in sub_results]
                results.extend(new_results)

        return results
        