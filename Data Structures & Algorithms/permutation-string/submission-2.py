class CharCounts:
    def __init__(self, s: str = ""):
        self._counts = [0] * 26
        for c in s:
            self.add(c)
            
    def add(self, c: str) -> None:
        i = ord(c) - ord('a')
        self._counts[i] += 1

    def remove(self, c: str) -> None:
        i = ord(c) - ord('a')
        assert self._counts[i] > 0
        self._counts[i] -= 1
        
    def equals(self, other: "CharCounts") -> bool:
        return self._counts == other._counts

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Check if s1 is in s2 (as a permutation)
        s1len = len(s1)
        s2len = len(s2)
        i = -1
        
        s1_counts = CharCounts(s1)
        window_counts = CharCounts(s2[:s1len])

        while i < s2len - s1len:
            i += 1

            # Initialize / update the current window
            if i > 0:
                window_counts.remove(s2[i-1])
                window_counts.add(s2[i + s1len - 1])

            # Check if s1 is a permutation of current window
            if window_counts.equals(s1_counts):
                return True

        return False



        