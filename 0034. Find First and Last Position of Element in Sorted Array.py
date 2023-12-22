class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ind = [-1, -1]
        c = 0
        while c<len(nums):
            if target == nums[c]:
                if ind[0] == -1:
                    ind[0] = c
                ind[1] = c
            c += 1
        return ind