class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        neg = False
        if x < 0 :
            neg = True
            s = s[:0:-1]
        else:
            s = s[::-1]
        if neg:
            out = - int(s)
        else:
            out = int(s)
        if out > - 2 ** 31 and out < 2 ** 31 + 1:
            return out
        else:
            return 0
        