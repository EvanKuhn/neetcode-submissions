class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Lowercase and remove non-alphanumeric chars
        fwd = "".join(c for c in s.lower() if c.isalnum())
        bak = fwd[::-1]
        return fwd == bak