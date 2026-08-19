
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values = set()
        for x in nums:
            if x in values:
                return True
            values.add(x)
        return False
