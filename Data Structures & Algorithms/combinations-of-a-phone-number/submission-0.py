class Solution:
    DIGIT_LETTERS = {
        "2": list("abc"),
        "3": list("def"),
        "4": list("ghi"),
        "5": list("jkl"),
        "6": list("mno"),
        "7": list("pqrs"),
        "8": list("tuv"),
        "9": list("wxyz"),
    }


    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        if len(digits) == 1:
            return self.DIGIT_LETTERS[digits[0]]
        results = []

        for c in self.DIGIT_LETTERS[digits[0]]:
            sub_results = self.letterCombinations(digits[1:])
            new_results = [c + r for r in sub_results]
            results.extend(new_results)

        return results
         

        