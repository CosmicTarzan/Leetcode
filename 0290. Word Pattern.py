class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        translate = {}
        arr = s.split()

        if len(pattern) != len(arr):
            return False

        for i in range(len(pattern)):
            if pattern[i] in translate.keys():
                if translate[pattern[i]] != arr[i]:
                    return False

            elif arr[i] not in translate.values():
                translate[pattern[i]] = arr[i]

            else:
                return False
                
        return True
