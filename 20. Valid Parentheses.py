class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'[': ']', '{': '}', '(': ')'}
        valid = True
        for i in s:
            if i in '[{(':
                stack.append(i)
            elif i in ')}]':
                if len(stack) == 0:
                    return False
                if i == d[stack[-1]]:
                    stack.pop()
                else:
                    break
        if len(stack) > 0:
            valid = False
        return valid
        