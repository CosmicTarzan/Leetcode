class Solution:
    def isHappy(self, n: int) -> bool:
        path = []
        while n not in path:
            if n == 1:
                return True
            path.append(n)
            s = 0
            while n > 0:
                s += (n % 10) ** 2
                n //= 10
            n = s
        return False
