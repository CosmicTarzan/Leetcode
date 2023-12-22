class Solution:
    def convert(self, s: str, numRows: int) -> str:
        outputTable = [[] for i in range(2 * numRows - 2)]
        output = ''
        if numRows == 1:
            return s
        for c, i in enumerate(s):
            if (c % (2 * numRows - 2)) < numRows:
                outputTable[(c % (2 * numRows - 2))].append(i)
            else:
                outputTable[-(c % (2 * numRows - 2))].append(i)
        for i in range(numRows):
            output += ''.join(outputTable[i])

        
        return output