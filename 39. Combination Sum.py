class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        
        def solve(nums, target, index, path):
            if target < 0:
                return
            if target == 0:
                ans.append(path)
                return
            for i in range(index, len(nums)):
                path2 = path.copy()
                path2.append(nums[i])
                solve(nums, target - nums[i], i, path2)

        solve(candidates, target, 0, [])
        return ans
