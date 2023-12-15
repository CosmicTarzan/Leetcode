class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        popped = 0
        for i in range(len(nums)):
            if nums[i - popped] == val:
                nums.pop(i - popped)
                popped += 1
        return len(nums)