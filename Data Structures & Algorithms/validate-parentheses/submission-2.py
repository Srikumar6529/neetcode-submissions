class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = '({['
        closed_brackets = ')}]'
        bracci = {
            "(":')',
            '{':'}',
            '[':']'
        }
        stack = []
        for bracket in s:
            if bracket in open_brackets:
                stack.append(bracket)
            else:
                if stack == []:
                    return False
                x = stack.pop()
                if bracci[x] != bracket:
                    return False
        return stack == []
