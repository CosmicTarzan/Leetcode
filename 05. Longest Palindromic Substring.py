class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        temp = ''
        for i in s:
            temp += i
            if temp == temp[::-1] and len(temp) > len(longest):
                longest = temp
            else:
                temp2 = list(temp)
                for j in temp[len(longest):]:
                    temp2.pop(0)
                    if temp2 == temp2[::-1] and len(temp2) > len(longest):
                        longest = ''.join(temp2)
        return longest
