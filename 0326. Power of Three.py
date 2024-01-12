class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n > 1:
            n /= 3
        if n == 1:
            return True
        return False
