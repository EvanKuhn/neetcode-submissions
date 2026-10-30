

def find_subset_of_len(nums: List[int], sslen: int) -> List[List[int]]:
    n = len(nums)
    results = []

    if sslen == 0:
        return [[]]

    for i in range(0, n):
        num = nums[i]
        #suffixes = find_subset_of_len(nums[0:i] + nums[i+1:], sslen-1)
        suffixes = find_subset_of_len(nums[i+1:], sslen-1)
        for x in suffixes:
            x.insert(0, num)
        results.extend(suffixes)

    return results




class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        for curlen in range(0, len(nums)+1):
            results.extend(find_subset_of_len(nums, curlen))
        return results
        