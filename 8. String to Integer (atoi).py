class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip(' ')
        neg = False
        if len(s) == 0:
            return 0
        if s[0] == '-':
            neg = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        if len(s) == 0:
            return 0
        if s[0].isdigit() == False:
            return 0
        cList = []
        for c in s:
            if c.isdigit():
                cList.append(c)
            else:
                break
        s = ''.join(cList)
        if neg:
            out = - int(s)
            if out < - 2 ** 31:
                return - 2 ** 31
        else:
            out = int(s)
            if out > 2 ** 31 - 1:
                return 2 ** 31 - 1
        return out