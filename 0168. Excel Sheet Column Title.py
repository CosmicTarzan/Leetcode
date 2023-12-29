class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while(columnNumber > 0):
            columnNumber -= 1
            c = columnNumber % 26
            columnNumber = columnNumber // 26
            ans.append(chr(c + ord('A')))
        
        return ''.join(ans[::-1])
