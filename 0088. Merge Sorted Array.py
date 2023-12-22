class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        arr = nums2
        i = 0
        while i < m:
            arr.append(nums1[i])
            i += 1
        arr.sort()
        i = 0
        while i < m + n:
            nums1[i] = arr[i]
            i += 1
