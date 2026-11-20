class Solution:
    def filter_nums(self, nums: List[int]) -> List[int]:
        # We only want at most 2 of any number, or 3 zeroes
        num_counts = defaultdict(int)
        for x in nums:
            num_counts[x] += 1
        results = []
        for num, count in num_counts.items():
            maxcount = 3 if num == 0 else 2
            for _ in range(min(count, maxcount)):
                results.append(num)
        return results


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = self.filter_nums(nums)
        n = len(nums)

        num_counts = defaultdict(int)
        for x in nums:
            num_counts[x] += 1

        results = set()

        for i in range(0, n-1):
            for j in range(i+1, n):
                num_i = nums[i]
                num_j = nums[j]
                need = 0 - num_i - num_j
                need_count = 1
                if need == num_i:
                    need_count +=1 
                if need == num_j:
                    need_count +=1 
                if num_counts[need] >= need_count:
                    results.add(tuple(sorted([num_i, num_j, need])))
                
        return [list(triple) for triple in results]

