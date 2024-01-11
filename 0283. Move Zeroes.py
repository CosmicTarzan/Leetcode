class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        popped = 0
        for i in range(len(nums)):
            if nums[i - popped] == 0:
                nums.pop(i - popped)
                popped += 1
                nums.append(0)
