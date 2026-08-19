from collections import defaultdict

def get_char_counts(s: str) -> defaultdict:
    '''Given a string, return a dict of char->count'''
    counts = defaultdict(int)
    for c in s:
        counts[c] += 1
    return counts


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Shortcut: check string lengths
        if len(s) != len(t):
            return False
        
        # Populate dicts of character counts
        s_chars = get_char_counts(s)
        t_chars = get_char_counts(t)

        return s_chars == t_chars
        