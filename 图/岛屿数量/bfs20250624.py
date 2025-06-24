class Solution:
    def __init__(self):
        self.directions = [[0,1],[0,-1],[1,0],[-1,0]]
        self.res = 0 # 岛屿的数量

    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if int(grid[i][j])==1 and not visited[i][j]:
                    self.res+=1
                    self.bfs(grid, visited, i, j)

        return self.res
    
    def bfs(self, grid, visited, i, j):
        queue = deque()
        queue.append((i, j))
        visited[i][j]=True

        while queue:
            x, y = queue.popleft()
            for dx, dy in self.directions:
                next_x, next_y = x+dx, y+dy
                if next_x<0 or next_y<0 or next_x>=len(grid) or next_y>=len(grid[0]):
                    continue
                if int(grid[next_x][next_y])==1 and not visited[next_x][next_y]:
                    visited[next_x][next_y]=True
                    queue.append((next_x, next_y))