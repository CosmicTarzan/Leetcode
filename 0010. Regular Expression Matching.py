class Solution:
  def isMatch(self, s: str, p: str) -> bool:
    mem = {}

    def solve(i: int, j: int) -> bool:
        if (i, j) in mem:
            return mem[(i, j)]
        if j == len(p):
            return i == len(s)

        first = i < len(s) and (p[j] == s[i] or p[j] == '.')

        if j + 1 < len(p) and p[j+1] == '*':
            ans = solve(i, j + 2) or (first and solve(i + 1, j))
        else:
            ans = first and solve(i + 1, j + 1)

        mem[(i, j)] = ans
        return ans

    return solve(0, 0)
