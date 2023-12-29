class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        i = 0
        for letter in reversed(columnTitle):
            ans += (ord(letter) - 64) * 26**i
            i += 1
        return ans
