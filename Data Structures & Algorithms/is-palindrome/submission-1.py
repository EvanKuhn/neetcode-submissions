class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = -1
        r = len(s)

        while l < r:
            l += 1
            r -= 1

            while l < r and not s[l].isalnum():
                l += 1
            
            while l < r and not s[r].isalnum():
                r -= 1

            if l < r:
                if s[l] != s[r]:
                    return False

        return True
