class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = dict()
        for i in strs:
            letters = ''.join(sorted(i))
            if letters in ans: ans[letters].append(i)
            else: ans[letters] = [i]
        return ans.values()