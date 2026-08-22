def inc_freq(arr: List, c: str) -> int:
    '''
    Given an array of character frequencies, increment the frequency
    for the given char. Assumes uppercase chars. Returns updated freq.
    '''
    assert len(arr) == 26
    assert len(c) == 1
    i = ord(c) - ord('A')
    arr[i] += 1
    return arr[i]


def dec_freq(arr: List, c: str) -> int:
    '''
    Given an array of character frequencies, deccrement the frequency
    for the given char. Assumes uppercase chars. Returns updated freq.
    '''
    assert len(arr) == 26
    assert len(c) == 1
    i = ord(c) - ord('A')
    arr[i] -= 1
    return arr[i]


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Use a sliding window. Maintain:
        # - l and r indexes (for window; character at s[r] is INCLUDED)
        # - character freqs
        # - count of most-frequent char
        # - count of other chars (can compute)

        char_freqs = [0] * 26
        max_char = ''
        max_char_freq = 0
        l = 0
        max_len = 0

        for r in range(0, len(s)):
            # Try adding next char (at r)
            new_char = s[r]
            freq = inc_freq(char_freqs, new_char)
            total_chars = (r - l) + 1

            # print("")
            # print(f"new_char: {new_char}")
            # print(f"freq: {freq}")
            # print(f"total_chars: {total_chars}")
            # print(f"char_freqs: {char_freqs}")

            # Check if we found a new max-freq char
            if freq > max_char_freq:
                max_char_freq = freq
                max_char = new_char
                # print(f"max_char={max_char} max_char_freq={max_char_freq}")
            
            # print(f"other chars: {total_chars - max_char_freq}")

            # If the total "other" chars is > k, we need to move the left side of the window
            while (total_chars - max_char_freq) > k:
                # Remove the leftmost char
                old_char = s[l]
                # print(f"removing {old_char}")
                freq = dec_freq(char_freqs, old_char)

                # Update max_char
                if old_char == max_char:
                    i, max_char_freq = max(enumerate(char_freqs), key=lambda x: x[1])
                    max_char = chr(ord('A') + char_freqs[i])

                # Move the left index
                l += 1
                total_chars -=1

            # Update the max substr len
            if total_chars > max_len:
                max_len = total_chars

        return max_len

    