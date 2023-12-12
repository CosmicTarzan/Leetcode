class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ''
        flag = False
        if strs[0] == '':
          return ''
        if len(strs) == 1:
          return strs[0]
        for i in range(len(strs[0])):
          for s in strs:
            if len(s) - 1 < i:
              flag = True
              break
            elif s[i] != strs[0][i]:
              flag = True
              break
          if not flag:
            pref += strs[0][i]
          else:
            break
        return pref
