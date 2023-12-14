class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def generate(l, r, s):
            if len(s) == n * 2:
                ans.append(s)
                return
            if l < n:
                generate(l + 1, r, s + '(')
            if r < l:
                generate(l, r + 1, s + ')')
        generate(0, 0, '')
        return ans