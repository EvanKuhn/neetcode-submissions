class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def get_counts(s: str) -> list[int]:
            counts = [0] * 26
            for c in s:
                i = ord(c) - ord('a')
                counts[i] += 1
            return counts
        s_counts = get_counts(s)
        t_counts = get_counts(t)
        return s_counts == t_counts
        
