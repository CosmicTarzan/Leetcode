# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        while (l < r):
            test = (l + r) // 2
            if (isBadVersion(test)):
                r = test
            else:
                l = test + 1
        return l
