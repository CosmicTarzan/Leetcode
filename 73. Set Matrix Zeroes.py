class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    if i not in rows: rows.append(i)
                    if j not in cols: cols.append(j)
        for i in rows:
            matrix[i] = [0] * len(matrix[0])
        for j in cols:
            for i in matrix:
                i[j] = 0 
