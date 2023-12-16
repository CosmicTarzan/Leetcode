class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    index = -1
    end = False
    for i in range(len(haystack)):
      if len(haystack[i:]) >= len(needle):
        contains = True
        for c, s in enumerate(needle):
          if haystack[i+c] == s:
            pass
          else:
            contains = False
            break
        if contains:
          index = i
          break
    return index