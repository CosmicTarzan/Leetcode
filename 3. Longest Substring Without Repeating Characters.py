class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charList = []
        longest = 0
        for i in s:
            if i in charList:
                if longest < len(charList):
                    longest = len(charList)
                while i in charList:
                    charList.pop(0)
            charList.append(i)
        if longest < len(charList):
            longest = len(charList)
        return longest