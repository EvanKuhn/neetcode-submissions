from enum import Enum

OPERATORS = "+-*/"

OP_FUNCS = {
    '+': lambda l, r: l + r,
    '-': lambda l, r: l - r,
    '*': lambda l, r: l * r,
    '/': lambda l, r: l / r,
}


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        # We should have an operator as the top token
        op = tokens.pop()

        # Get the value of the right expression
        # - If we see an operator, do a recursive call that will
        #   pop off all elements of the right-hand-side
        if tokens[-1] in OPERATORS:
            right = self.evalRPN(tokens)
        else:
            right = int(tokens.pop())

        # Get the value of the left expression
        # - Same deal as above for RHS
        if tokens[-1] in OPERATORS:
            left = self.evalRPN(tokens)
        else:
            left = int(tokens.pop())

        # Apply operator
        return int(OP_FUNCS[op](left, right))
