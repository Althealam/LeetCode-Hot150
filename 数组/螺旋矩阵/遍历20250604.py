# 时间复杂度：O(mn)，m和n分别是输入矩阵的行数和列数
# 空间复杂度：O(1)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[] # 需要返回的元素
        m, n = len(matrix), len(matrix[0]) # m行n列
        left, right, top, bottom = 0, n-1, 0, m-1
        while left<=right and top<=bottom:
            # 遍历上面的一行
            for j in range(left, right+1):
                ans.append(matrix[top][j])
            # 遍历右边的一列
            for i in range(top+1, bottom+1): # 这里必须是top+1，否则会和上面的一行的最后一个元素重复
                ans.append(matrix[i][right]) 
            if top<bottom and left<right: # 当上下不在同一行，左右不在同一列的时候才执行，否则会导致重复元素的出现
                # 遍历下面的一行
                for j in range(right-1, left, -1):
                    ans.append(matrix[bottom][j])
                # 遍历左边的一列
                for i in range(bottom, top, -1):
                    ans.append(matrix[i][left])
            left, right, top, bottom = left+1, right-1, top+1, bottom-1
        return ans
        