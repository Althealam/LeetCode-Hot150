# 1. dp数组以及下标的含义：dp[i][j]表示从[0,0]移动到[i,j]的不同路径数量为dp[i][j]
# 2. 递推公式：
# dp[i][j]=dp[i-1][j]+dp[i][j-1]
# 3. 初始化：
# if obstacleGrid[0][0]!=1: dp[0][0]=1
# dp[i][0]=1 dp[0][j]=1 
# if obstacleGrid[i][j]==1: dp[i][j]=0
# 4. 遍历顺序：从前向后，从左向右
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp=[[0]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        if obstacleGrid[0][0]==1 or obstacleGrid[-1][-1]==1:
            return 0
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0]==1:
                break
            else:
                dp[i][0]=1
        
        for j in range(len(obstacleGrid[0])):
            if obstacleGrid[0][j]==1:
                break
            else:
                dp[0][j]=1

        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j]==1:
                    continue
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        
        return dp[-1][-1]
        