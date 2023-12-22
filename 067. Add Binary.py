class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ans = ''
        c1, c2 = len(a) - 1, len(b) - 1

        while c1 >=0 or c2 >= 0 or carry > 0:
            if c1 >= 0:
                carry += int(a[c1])
                c1 -= 1
            if c2 >= 0:
                carry += int(b[c2])
                c2 -= 1 
            ans += str(carry % 2)
            carry //= 2
            
        return ans[::-1]
