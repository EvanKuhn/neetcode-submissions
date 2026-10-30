# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         return self.subsets(nums)

#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         if not nums:
#             return []

#         if len(nums) == 1:
#             return [nums]

#         results = []

#         for i in range(0,len(nums)):
#             value = nums[i]

#             # Sub-results including the current number
#             sub_results = self.subsetsWithDup(nums[i+1:])
#             new_results = [[value] + s for s in sub_results]
#             results.extend(new_results)


#             # Sub-results excluding the current number
#             # - Once you exclude a number, don't include future instances
#             #   (i.e. duplicates) of that number
#             j = i
#             while j < len(nums) and nums[j] == value:
#                 j += 1
#             sub_results = self.subsetsWithDup(nums[j:])
#             results.extend(sub_results)
            
#         return results







class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = [[]]

        # Generate all possible results
        for x in nums:
            results = results + [r + [x] for r in results]

        # Put into a set
        tuples = [tuple(sorted(r)) for r in results]
        uniqs = set(tuples)
        return [list(x) for x in uniqs]