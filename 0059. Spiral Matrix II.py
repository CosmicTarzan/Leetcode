class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        i, j, ei, ej = 0, 0, 0, 1
        for k in range(n*n):
            ans[i][j] = k + 1
            if ans[(i + ei) % n][(j + ej) % n]:
                ei, ej = ej, -ei
            i += ei
            j += ej
        return ans
