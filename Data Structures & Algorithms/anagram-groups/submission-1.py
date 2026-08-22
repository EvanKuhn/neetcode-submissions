from collections import defaultdict


def get_freqs(s: str) -> tuple:
    '''
    Convert a string to a tuple of integers of length 26, containing
    the frequencies of chars a-z. Assumes lowercase.
    '''
    freqs = [0] * 26
    for c in s:
        i = ord(c) - ord('a')
        freqs[i] += 1
    return tuple(freqs)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Steps:
        # 1. Convert strings to frequency tuples
        # 2. Group strings by freq-tuples, via dict
        #    - Strings with identical character freqs are anagrams
        # 3. Return the dict's values
        freqs_to_strs_map = defaultdict(list)
        for s in strs:
            freqs_to_strs_map[get_freqs(s)].append(s)
        return list(freqs_to_strs_map.values())
