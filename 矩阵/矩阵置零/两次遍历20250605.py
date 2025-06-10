# 时间复杂度：O(m+n) m为行，n为列
# 空间复杂度：O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0])
        row_zero=set()
        col_zero=set()
        # 存储含有0的行和列
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    row_zero.add(i)
                    col_zero.add(j)
        for i in range(row):
            for j in range(col):
                if i in row_zero or j in col_zero:
                    matrix[i][j]=0