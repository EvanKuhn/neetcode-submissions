class Solution:
    def is_palindrome(self, s: str) -> bool:
        n = len(s)
        for i in range(0, n//2):
            if s[i] != s[n-i-1]:
                return False
        return True

    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        if len(s) == 1:
            return [[s]]
        results = []
        for i in range(1,len(s)+1):
            token = s[:i]
            if not self.is_palindrome(token):
                continue
            sub_partitions = self.partition(s[i:])
            new_partitions = [[token] + p for p in sub_partitions]
            results.extend(new_partitions)
        return results
