class Solution:
    def countSubstrings(self, s: str) -> int:
        pals = []
        
        def search_odd(s: str, i: int) -> int:
            n = len(s)
            a = i
            b = i
            count = 1

            while True:
                if a == 0 or b == n-1:
                    break
                if s[a-1] == s[b+1]:
                    a -= 1
                    b += 1
                    count += 1
                else:
                    break

            return count


        def search_even(s: str, i: int) -> int:
            n = len(s)
            a = i
            b = i+1
            
            if i == n-1 or s[a] != s[b]:
                return 0
            count = 1

            while True:
                if a == 0 or b == n-1:
                    break
                if s[a-1] == s[b+1]:
                    a -= 1
                    b += 1
                    count += 1
                else:
                    break
            
            return count

        total = 0
        for i in range(0, len(s)):
            total += search_odd(s, i)
            total += search_even(s, i)

        return total