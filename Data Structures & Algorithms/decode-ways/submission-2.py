
Result = namedtuple('Result', ['count', 'valid'])

class Solution:
    def numDecodings(self, s: str) -> int:
        # Thoughts:
        # - Dynamic Programming. 
        # - You have 1 or 2 options at each iteration:
        #   1: choose the first char, and count decodings 
        #      for remaining chars, as long as they don't 
        #      start with '0'.
        #   2. Choose first two chars, and count decodings
        #      for remaining chars.
        
        memo = {}

        def solve(s: str) -> Result:
            n = len(s)

            if s.startswith('0'):
                return Result(0, False)
            if n < 2:
                return Result(1, True)

            if s not in memo:
                r1 = solve(s[1:])
                count1 = r1.count if r1.valid else 0

                if int(s[:2]) <= 26:
                    r2 = solve(s[2:])
                else:
                    r2 = Result(0, False)
                count2 = r2.count if r2.valid else 0
                
                count = count1 + count2
                valid = r1.valid or r2.valid

                memo[s] = Result(count, valid)

            return memo[s]

        res = solve(s)
        return res.count if res.valid else 0