class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quads = []
        for j in range(len(nums) - 3):
            if j>0 and nums[j] == nums[j-1]:
                continue
            for i in range(j + 1, len(nums) - 2):
                if i>j+1 and nums[i] == nums[i-1]:
                    continue
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    su = nums[j] + nums[i] + nums[l] + nums[r]
                    if su < target:
                        l += 1
                    elif su > target:
                        r -= 1
                    else:
                        quad = [nums[j], nums[i], nums[l], nums[r]]
                        quads.append(quad)
                        while l < r and nums[l] == quad[2]:
                            l += 1
                        while l < r and nums[r] == quad[3]:
                            r -= 1
        return quads