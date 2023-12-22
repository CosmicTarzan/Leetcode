class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        if rowIndex == 0:
            ans = [1]
        elif rowIndex == 1:
            ans = [1,1]
        else:
            for n in range(rowIndex):
                ans = [1] + [ans[i] + ans[i+1] for i in range(n)] + [1]
        return ans
