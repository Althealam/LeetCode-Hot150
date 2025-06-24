# 本题相当于是沉没孤岛

# 思路：
# 1. 遍历四条边，将所有的岛屿变成#（也就是把所有的O变成#）
# 2. 遍历整个棋盘，将所有的O变成X，将#变成O
class Solution:
    def __init__(self):
        self.directions = [[0,1],[0,-1],[1,0],[-1,0]]

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 1. 遍历四条边界，标记所有与边界相连的O为#
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i==0 or i==len(board)-1 or j==0 or j==len(board[0])-1) and board[i][j]=='O':
                    board[i][j]='#'
                    self.dfs(board, i, j)
            
        # 2. 遍历整个棋盘，将所有的O变成X，将#变成O
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='#':
                    board[i][j]='O'
        
    
    def dfs(self, board, i, j):
        for dx, dy in self.directions:
            next_x = i+dx
            next_y = j+dy
            if next_x<0 or next_y<0 or next_x>=len(board) or next_y>=len(board[0]):
                continue
            if 0<=next_x<=len(board)-1 and 0<=next_y<=len(board[0])-1 and board[next_x][next_y]=='O':
                board[next_x][next_y]='#'
                self.dfs(board, next_x, next_y)
