class Solver:
    def __init__(self, open_avail: int, close_avail: int, value: str = "") -> None:
        self.open_avail = open_avail
        self.close_avail = close_avail
        self.value = value

    def done(self) -> bool:
        return self.open_avail == 0 and self.close_avail == 0

    def iterate(self) -> List["Solver"]:
        if self.done():
            return [self]
        results = []
        # We can always add an open paren, if any are available
        if self.open_avail > 0:
            results.append(Solver(self.open_avail-1, self.close_avail, self.value + "("))
        # We can add a close paren as long as it has a corresponding open in the expression
        if self.close_avail > self.open_avail:
            results.append(Solver(self.open_avail, self.close_avail-1, self.value + ")"))

        return results

    def __str__(self) -> str:
        return f"Solver(open_avail={self.open_avail}, close_avail={self.close_avail}, value=\"{self.value}\")"


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        exprs = [Solver(n, n)]

        while exprs:
            x = exprs.pop()
            if x.done():
                results.append(x)
            else:
                exprs.extend(x.iterate())

        return [r.value for r in results]
