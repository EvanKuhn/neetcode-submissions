

class CharCounter:
    def __init__(self, k: int):
        self.k = k
        self.char_counts = [0] * 26
        self._length = 0
        self._max_char = ''
        self._max_char_count = 0

    def add(self, c: str) -> None:
        i = ord(c) - ord('A')
        self.char_counts[i] += 1
        self._length += 1
        if self.char_counts[i] > self._max_char_count:
            self._max_char = c
            self._max_char_count = self.char_counts[i]
            
    def remove(self, c: str) -> None:
        i = ord(c) - ord('A')
        assert(self.char_counts[i] > 0)
        self.char_counts[i] -= 1
        self._length -= 1
        if c == self._max_char:
            # TODO: can do in one pass
            max_count = max(self.char_counts)
            i = self.char_counts.index(max_count)  
            self._max_char = chr(ord('A') + i)
            self._max_char_count = max_count

    def length(self) -> int:
        return self._length

    def is_valid(self) -> bool:
        '''Return a bool indicating if we have k or fewer "other" characters'''
        return self.other_char_count() <= self.k
         
    def max_char(self) -> str:
        return self._max_char

    def max_char_count(self) -> int:
        return self._max_char_count

    def other_char_count(self) -> int:
        return (self._length - self._max_char_count)
    

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        n = len(s)
        maxlen = 0
        counter = CharCounter(k)

        while r < n:
            c = s[r]
            counter.add(c)

            # If we have a valid substring, update maxlen
            if counter.is_valid():
                maxlen = max(maxlen, counter.length())

            # Otherwise, remove characters until the counter is valid again
            else:
                while not counter.is_valid():
                    counter.remove(s[l])
                    l += 1
                assert l <= r
        
            # Increment r
            r += 1

        return maxlen

                
        