class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        popped = 0
        for i in range(len(nums)):
            if i > 0 and nums[i - popped] == nums[i - 1 - popped]:
                popped += 1
                nums.pop(i - popped)
        return len(nums)
