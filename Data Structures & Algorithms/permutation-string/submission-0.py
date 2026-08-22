
def to_index(c: str) -> int:
    assert len(c) == 1, f"str '{c}' must have length 1"
    i = ord(c) - ord('a')
    assert 0 <= i < 26, f"char {c} => index {i} is not in range [0,26)"
    return i


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Error checking
        if len(s1) > len(s2):
            return False

        # Store character frequencies as arrays
        k = len(s1)
        s1_freqs = [0] * 26
        s2_freqs = [0] * 26

        # Populate s1 and s2 freqs array
        for i in range(0, k):
            s1_freqs[to_index(s1[i])] += 1
            s2_freqs[to_index(s2[i])] += 1

        # print(s1_freqs)
        # print(s2_freqs)

        # Did we find it at the front?
        if s1_freqs == s2_freqs:
            return True

        # print(f"s1 = {s1}")
        # print(f"s2 = {s2}")
        # print(s1_freqs)

        # Move a sliding window and check character freqs
        l, r = 1, k
        while r < len(s2):
            # Decrement the previous char (at l-1) and increment the new char (at r)
            s2_freqs[to_index(s2[l-1])] -= 1
            s2_freqs[to_index(s2[r  ])] += 1
            #print(s2_freqs)

            # Check for match
            if s1_freqs == s2_freqs:
                return True 

            # Move indexes
            l += 1
            r += 1

        return False        
        