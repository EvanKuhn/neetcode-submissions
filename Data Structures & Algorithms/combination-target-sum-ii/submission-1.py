class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort candidates so we can skip duplicates
        candidates.sort()
        return self.comboSum(candidates, target)


    def comboSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        for i in range(0, len(candidates)):
            # If we skipped the previous number and it's the same, then skip this one too.
            # - If we "used" previous value, it would have been removed from the candidates list.
            if i > 0 and candidates[i] == candidates[i-1]:
                continue

            value = candidates[i]
            remaining = candidates[i+1:]

            if value == target:
                results.append([value])
            elif value < target:
                sub_results = self.comboSum(remaining, target-value)
                new_results = [[value] + s for s in sub_results]
                results.extend(new_results)
        
        return results
