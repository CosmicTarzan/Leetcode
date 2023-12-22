class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = 0
        for i in digits:
            n = (n * 10) + i
        n += 1
        ans = []
        while n > 0:
            ans.insert(0, n % 10)  
            n //= 10 
        return ans
