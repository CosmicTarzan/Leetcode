class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ind = -1
        c = 0
        while c<len(nums):
            if target == nums[c]:
                return c
            c += 1
        return ind