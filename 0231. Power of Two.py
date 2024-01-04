class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        t = 1
        while n >= t:
            if t == n:
                return True
            t *= 2
        return False
