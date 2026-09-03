class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        results = []

        if n == 1:
            return [[nums[0]]]

        for i in range(0,n):
            value = nums[i]
            rest = nums[0:i] + nums[i+1:]
            sub_perms = self.permute(rest)
            new_results = [[value] + p for p in sub_perms]
            results.extend(new_results)
        
        return results