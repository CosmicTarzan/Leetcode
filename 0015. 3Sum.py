class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums) - 2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                su = nums[i] + nums[l] + nums[r]
                if su < 0:
                    l += 1
                elif su > 0:
                    r -= 1
                else:
                    tri = [nums[i], nums[l], nums[r]]
                    triplets.append(tri)
                    while l < r and nums[l] == tri[1]:
                        l += 1
                    while l < r and nums[r] == tri[2]:
                        r -= 1
        return triplets