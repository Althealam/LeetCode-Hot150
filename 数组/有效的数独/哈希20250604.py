# 目标：
# （1）每一行不能有重复的数字
# （2）每一列不能有重复的数字
# （3）每个3x3的小方块不能有重复的数字
# 思路：哈希
# 1. row[i][num]表示第i行是否出现过数字num+1
# 2. col[j][num]表示第j列是否出现过数字num+1
# 3. block[b][num]表示第b个3x3的块是否出现过数字num+1

# 时间复杂度：O(1)
# 空间复杂度：O(1)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[[0]*9 for _ in range(9)]  # 表示该元素没有出现过
        col=[[0]*9 for _ in range(9)]  
        block=[[0]*9 for _ in range(9)] 

        for i in range(9):
            for j in range(9):
                if board[i][j]!='.': # 如果是空格则跳过
                    num=int(board[i][j])-1 # 把数字转换为索引
                    b=(i//3)*3+j//3  # 计算当前格子所属的3x3的小方块编号
                    if row[i][num] or col[j][num] or block[b][num]: 
                        # 如果该数字已经在对应的行、列或者小方块中出现过了，则返回False
                        return False
                    # 如果该数字没有在对应的行、列或者小方块中出现，则标记为已出现
                    row[i][num]=col[j][num]=block[b][num]=1
        return True
        