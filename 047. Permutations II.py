class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def next(nr):
            if nr == len(nums):
                ans.add(tuple(nums[:]))
            for i in range(nr, len(nums)):
                nums[nr], nums[i] = nums[i], nums[nr]
                next(nr + 1)
                nums[nr], nums[i] = nums[i], nums[nr]
        next(0)
        return ans
