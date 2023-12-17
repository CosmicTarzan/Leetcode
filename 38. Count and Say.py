class Solution:
    def countAndSay(self, n: int) -> str:
        def solve(passedN):
            if passedN == '':
                return '1'
            number = 0
            count = 0
            ans = ''
            for i in str(passedN):
                if i != number:
                    if number:
                        ans += str(count) + number
                    number = i
                    count = 1
                else:
                    count += 1 
            ans += str(count) + number
            return ans
        ans = ''
        for i in range(n):
            ans = solve(ans)
        return ans
