class Solution:
    OPEN_PARENS = ['(', '{', '[']
    CLOSE_PARENS = [')', '}', ']']
    MATCHING_PAREN = dict(zip(CLOSE_PARENS, OPEN_PARENS))

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            # Open paren: add to stack
            if c in self.OPEN_PARENS:
                stack.append(c)
            # Closing paren: make sure last paren matches,
            # and remove it from the stack
            elif c in self.CLOSE_PARENS:
                if not stack or stack[-1] != self.MATCHING_PAREN[c]:
                    return False
                stack = stack[:-1]

        return len(stack) == 0