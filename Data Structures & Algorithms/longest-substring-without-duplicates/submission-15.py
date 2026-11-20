class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        # Indexes of first and last char of the current window.
        # - Increment j until we encounter a duplicate character
        # - Then increment i until no duplicate characters are found
        # - Always update the max length found
        i = 0
        j = 0
        maxlen = 1
        chars = set([s[0]])

        while j < len(s)-1:
            j += 1

            # If we found a repeating character, increment i and remove
            # each character we pass.
            if s[j] in chars:
                while True:
                    chars.remove(s[i])
                    # print(f"removing {s[i]} => {chars}")
                    found = s[i] == s[j]
                    i += 1
                    if found:
                        # print("-found match")
                        break
            
            # Add the new character at index j
            chars.add(s[j])
            # print(f"adding {s[j]} => {chars}")
            maxlen = max(maxlen, len(chars))

        return maxlen





