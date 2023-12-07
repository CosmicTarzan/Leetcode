class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for c, i in enumerate(nums):
            for d, j in enumerate(nums[c+1:]):
                if i + j == target:
                    return [c, d+c+1]