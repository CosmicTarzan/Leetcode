class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def next(nr):
            if nr == len(nums):
                ans.append(nums.copy())
            for i in range(nr, len(nums)):
                nums[nr], nums[i] = nums[i], nums[nr]
                next(nr + 1)
                nums[nr], nums[i] = nums[i], nums[nr]
        next(0)
        return ans
