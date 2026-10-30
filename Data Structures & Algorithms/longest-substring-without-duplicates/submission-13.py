class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l = 0
        r = 0
        n = len(s)
        seen = set()
        maxlen = 0

        while r < n:
            c = s[r]
            # print(f"c = {c}")
            if c in seen:
                # Found a duplicate character. Update maxlen.
                maxlen = max(len(seen), maxlen)

                # Move l and remove characters until we remove the same char as at r
                while l < r:
                    lchar = s[l]
                    l += 1
                    if lchar != c:
                        seen.remove(lchar)
                        # print(f"removing {lchar} => {seen}")
                    else:
                        break
            else:
                # Found a new character
                seen.add(c)
                # print(f"adding {c} => {seen}")
            r += 1   

        maxlen = max(len(seen), maxlen)
        return maxlen
        