from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def sort_chars(s: str) -> str:
            # initialize char counts array
            counts = [0] * 26
            for c in s:
                i = ord(c) - ord('a')
                counts[i] += 1

            # Convert char counts to a string of chars in alphabetical order
            result = ""
            for i in range(len(counts)):
                if counts[i] > 0:
                    c = chr(i + ord('a'))
                    result += (c * counts[i])
            return result

        # Construct dict of sorted-chars, to list of original strings
        anagrams = defaultdict(list)
        for s in strs:
            sorted = sort_chars(s)
            anagrams[sorted].append(s)

        # Return the lists of original strings from the anagrams dict
        return list(anagrams.values())

