# 思路：
# 顺时针旋转90度，位于(i,j)的元素的位置去到(j, n-1-i)
# 竖着看：1. 第一列的元素去到第一行 2. 第二列的元素去到第二行 3. 第j列的元素去到第j行==>原本的(i,j)变成了(j,x)
# 横着看：1. 第一行的元素去到最后一列 2. 第二行的元素去到倒数第二列 3. 第i行的元素去到第n-1-i行==>(i,j)变成了(j, n-1-i)
# (i,j)->(j, n-1-i)可以通过两次翻转得到：(i,j)->(j,i)->(j,n-1-i)
# （1）转置：把矩阵按照主对角线翻转，位于(i,j)的元素去到(j,i)
# （2）行翻转：把每一行的内部元素翻转，位于(j,i)的元素去到(j,n-1-i)

# 时间复杂度：O(n**2)
# 空间复杂度：O(1)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        # 1. 转置：(i,j)->(j,i)
        for i in range(n):
            for j in range(i): # 遍历对角线下方的元素
                matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]
        # 2. 行翻转
        for row in matrix:
            row.reverse()
        