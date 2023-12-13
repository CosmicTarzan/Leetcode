class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 99999
        for i in range(len(nums) - 2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                su = nums[i] + nums[l] + nums[r]
                if abs(ans - target) > abs(su - target):
                    ans = su
                if su < target:
                    l += 1
                elif su > target:
                    r -= 1
                else:
                    ans = target
                    break
            if ans - target == 0: 
                break
        return ans