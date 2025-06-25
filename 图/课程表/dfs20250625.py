# 题意：给定一个有向图，判断图中是否有环，如果有的话则返回False，否则的话返回True
# 思路：对于每个节点x，定义三种颜色值，0表示节点x尚未被访问到，1表示节点x正在访问中，dfs(x)尚未结束，2表示节点x已经访问完毕，dfs(x)已经返回
# 1. 建图：把每个prerequisites[i]=[a,b]看成一条有向边，表示b->a，构建一个有向图grid
# 2. 创建长为numCourses的颜色数组colors，所有元素值初始化为0，表示每个元素的颜色值
# 3. 遍历colors，如果colors[x]=0，则调用递归函数dfs(x)
# 3.1: 标记colors[x]=1，表示该节点正在访问中
# 3.2: 遍历x的邻居y：如果colors[y]==1则找到了环，直接返回True；如果colors[y]==0并且dfs(y)==True，那么dfs(x)返回True
# 3.3: 如果没有找到环，那么先标记colors[x]=2，表示x已经完全访问完毕，返回False
# 4. 如果dfs(x)返回True，那么找到了环，返回False；如果遍历完所有节点都没有找到环，那么返回True

# 时间复杂度：O(n+m)，其中n是numCourses，m是prerequisites的长度。每个节点至多递归访问一次，每条边至多遍历一次
# 空间复杂度：O(n+m)，存储grid需要n+m的空间

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        grid = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            grid[b].append(a) # 表示b可以由a导到
        
        color = [0]*numCourses
        def dfs(x):
            color[x]=1 # x正在访问中
            for y in grid[x]:
                if color[y]==1 or color[y]==0 and dfs(y):
                    return True # 找到了环
            color[x]=2 # x完全访问完毕
            return False # 没有找到环
        
        for i, c in enumerate(color):
            if c==0 and dfs(i):
                return False # 有环
        return True # 没有环