# 时间复杂度：O(mn)，其中m和n分别为board的行数和列数
# 空间复杂度：O(1)

# 规则：
# 规则1: 如果活细胞周围八个位置的活细胞数少于两个，则该位置的活细胞死亡==>将细胞值改为1，表示这个细胞过去是活的现在死了
# 规则2: 如果活细胞周围八个位置有两个或者三个活细胞，则该位置的细胞仍然存活，不改变其值
# 规则3: 如果活细胞周围八个位置有超过三个活细胞，则该位置的活细胞死亡==>将细胞值改为-1，表示这个细胞过去是活的现在死了
# 规则4: 如果死细胞周围正好有三个活细胞，则该位置死细胞复活==>将细胞值改为2，表示这个细胞获取是死的现在活了
# 最后将状态为2的细胞修改为1，状态为-1的细胞修改为0
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors=[(1,0), (-1,0), (0,1), (0,-1), (1,-1), (1,1), (-1, 1), (-1,-1)]
        rows=len(board)
        cols=len(board[0])
        # 遍历面板内的每一个格子内的细胞    
        for row in range(rows):
            for col in range(cols):
                # 对于每个细胞，统计其活细胞的数量
                live_neighbors=0
                for neighbor in neighbors:
                    # 相邻位置的坐标
                    r=row+neighbor[0] # 横坐标
                    c=col+neighbor[1] # 纵坐标
                    # 确保横纵坐标没有过界并且查看相邻的细胞是否是活细胞
                    if (r<rows and r>=0) and (c<cols and c>=0) and abs(board[r][c])==1:
                        live_neighbors+=1
                
                # 规则1或者规则3
                if board[row][col]==1 and (live_neighbors<2 or live_neighbors>3):
                    # -1表示这个细胞过去是活着的，现在死了
                    board[row][col]=-1
                
                # 规则4
                if board[row][col]==0 and live_neighbors==3:
                    # 2表示这个细胞过去是死的，现在活了
                    board[row][col]=2
            
        # 遍历board得到一次更新后的状态
        for row in range(rows):
            for col in range(cols):
                if board[row][col]>0:
                    board[row][col]=1
                else:
                    board[row][col]=0