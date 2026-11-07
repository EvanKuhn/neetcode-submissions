class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        memo = {}

        def search(s: str) -> bool:
            nonlocal wordset, memo

            # Base case
            if not s or s in wordset:
                return True

            
            if s not in memo:
                solutions = []

                # Search all possibilities
                for word in wordDict:
                    if s.startswith(word):
                        remaining = s[len(word):]
                        solutions.append(search(remaining))

                # Record if we found at least one solution, or not
                memo[s] = (True in solutions)

            return memo[s]

        return search(s)