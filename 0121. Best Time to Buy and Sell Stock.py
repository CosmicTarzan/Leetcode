class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        low = prices[0]
        for i in range(1,len(prices)):
            low = min(low, prices[i])
            diff = max(diff, prices[i]- low)
        return diff
