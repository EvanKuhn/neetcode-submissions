# Naive-ish Solution
# - start at each index
# - grow out and check for palindrome

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_strs = []
        max_len = 0
        
        # def is_palindrome(s: str, first: int, last: int) -> bool:
        #     if first == last:
        #         return True
        #     i = first
        #     j = last
        #     while i < j:
        #         if s[i] != s[j]:
        #             return False
        #         i += 1
        #         j -= 1
        #     return True

        def search_odd(s: str, i: int) -> str:
            n = len(s)
            a = i
            b = i

            while True:
                if a == 0 or b == n-1:
                    break
                if s[a-1] == s[b+1]:
                    a -= 1
                    b += 1
                else:
                    break

            return s[a:b+1]


        def search_even(s: str, i: int) -> str:
            n = len(s)
            a = i
            b = i+1

            if i == n-1 or s[a] != s[b]:
                return ""

            while True:
                if a == 0 or b == n-1:
                    break
                if s[a-1] == s[b+1]:
                    a -= 1
                    b += 1
                else:
                    break
            
            return s[a:b+1]

        for i in range(0, len(s)):
            max_odd = search_odd(s, i)
            max_even = search_even(s, i)

            if len(max_odd) > max_len:
                max_strs = [max_odd]
                max_len = len(max_odd)
            elif len(max_odd) == max_len:
                max_strs.append(max_odd)

            if len(max_even) > max_len:
                max_strs = [max_even]
                max_len = len(max_even)
            elif len(max_even) == max_len:
                max_strs.append(max_even)

        return max_strs[0] if max_strs else ""




                
