

# Using dict
# class CharCounts: 
#     def __init__(self, s: str = "") -> None:
#         self._counts = defaultdict(int)
#         for c in s:
#             self.add(c)

#     def add(self, c: str) -> None:
#         self._counts[c] += 1

#     def remove(self, c: str) -> None:
#         assert(self._counts[c] > 0)
#         self._counts[c] -= 1

#     def contains(self, other: "CharCounts") -> bool:
#         for c in other._counts.keys():
#             if self._counts[c] < other._counts[c]:
#                 return False
#         return True


class CharCounts:
    NUM_CHARS = 1 + ord('z') - ord('A')

    def __init__(self, s: str = "") -> None:
        self._counts = [0] * self.NUM_CHARS
        for c in s:
            self.add(c)

    def add(self, c: str) -> None:
        i = ord(c) - ord('A')
        self._counts[i] += 1

    def remove(self, c: str) -> None:
        i = ord(c) - ord('A')
        assert self._counts[i] > 0
        self._counts[i] -= 1

    def contains(self, other: "CharCounts") -> bool:
        for i in range(0, self.NUM_CHARS):
            if self._counts[i] < other._counts[i]:
                return False
        return True


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Check if T is in S
        l = 0
        r = -1
        s_len = len(s)
        t_len = len(t)
        minlen = s_len + 1
        minlen_str = ""
        minlen_l = 0
        minlen_r = -1

        print(f"s_len = {len(s)}")
        print(f"t_len = {len(t)}")

        t_counts = CharCounts(t)
        window_counts = CharCounts()
        # print(t_counts._counts)
        # print(window_counts._counts)


        # Optimize: add first len(t)-1 chars from s to counter
        for i in range(0, t_len-1):
            r = i
            window_counts.add(s[r])

        while r < s_len-1 and l <= s_len - t_len:
            # Increment r and add new character
            r += 1
            window_counts.add(s[r])

            # If the window now contains t's characters, move the left pointer
            # until it doesn't.
            while window_counts.contains(t_counts): 
                # Update minimum valid window
                winlen = r - l + 1
                if winlen < minlen:
                    minlen = winlen
                    minlen_l = l
                    minlen_r = r
                    #minlen_str = s[l:r+1]

                # Move l pointer
                window_counts.remove(s[l])
                l += 1
        
        #return minlen_str
        return s[minlen_l:minlen_r+1]

                



