class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}
        for i in range(len(nums)):
            if nums[i] in map.keys():
                map[nums[i]].append(i)
            else:
                map[nums[i]] = [i]
        for key, value in map.items():
            if type(value) == list:
                last = value[0]
                for i in value[1:]:
                    if i - last <= k:
                        return True
                    last = i
        return False
