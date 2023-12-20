class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -999999
        current = 0
        for i in nums:
            current += i
            if current > ans:
                ans = current
            if current < 0:
                current = 0
        return ans
