class Solution:
    def isValid(self, s: str) -> bool:
        parens = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        stack = []

        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            elif len(stack) == 0 or c != parens[stack.pop()]:
                return False

        return len(stack) == 0
