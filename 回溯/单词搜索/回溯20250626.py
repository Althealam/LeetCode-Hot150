# 思路：枚举i=0,1,2,...,m-1和j=0,1,2,...,n-1，以(i,j)为起点开始搜索
# dfs(i,j,k)表示当前在board[i][j]这个格子，要匹配word[k]，返回在这个状态下是否可以匹配成功
# （1）board[i][j]=word[k]：匹配失败
# （2）如果k=len(word)-1，匹配成功，返回True
# （3）枚举(i,j)周围的四个相邻格子(x,y)，如果(x,y)没有出界，则递归dfs(x,y,k+1)，如果其返回True，则dfs(x,y,k)也返回True
# （4）如果递归的四个格子都没有返回True，则返回False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(i, j, k):
            if board[i][j]!=word[k]: # 匹配失败
                return False
            if k==len(word)-1: # 匹配成功
                return True
            board[i][j]='' # 标记为访问过
            for x,y in (i, j-1), (i, j+1), (i-1, j), (i+1, j): # 相邻格子
                if 0<=x<m and 0<=y<n and dfs(x, y, k+1):
                    return True # 搜到了
            board[i][j] = word[k] # 恢复现场
            return False # 没搜到
        return any(dfs(i, j, 0) for i in range(m) for j in range(n))
        