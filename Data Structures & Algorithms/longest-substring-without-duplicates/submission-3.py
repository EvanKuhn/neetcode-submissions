class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Error checking
        if not s:
            return 0

        # Maintain two indexes, i and j
        i = 0

        # Maintain a set of chars we've seen as a map from char to index
        seen_char_to_index = {s[0]: 0}

        # Maintain longest substr seen
        max_len = 1

        # Walk until we reach the end
        for j in range(1, len(s)):
            # Get next char at index j
            new_char = s[j]
            #print(f"next char: {new_char}")

            # If we found a duplicate, move i to one past the previous index
            # of that char, and remove all chars from the 'seen' map.
            if new_char in seen_char_to_index:
                new_i = seen_char_to_index[new_char] + 1
                while i < new_i:
                    #print(f"removing {s[i]}")
                    del seen_char_to_index[s[i]]
                    i += 1

            # Add the newly-found char
            #print(f"adding {new_char} => {len(seen_char_to_index)+1}")
            seen_char_to_index[new_char] = j

            # Update the longest substr
            cur_len = len(seen_char_to_index)
            if cur_len > max_len:
                #print(f"new max_len={cur_len}")
                max_len = cur_len
        
        return max_len

