"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# 思路：遍历整个图，遍历的时候要记录已经访问的节点，所以用lookup来记录
# 1. 当前节点是None，直接return
# 2. 复制当前根节点
# 3. 复制根节点的左子树
# 4. 复制根节点的右子树
# 5. 返回复制后的根节点

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        lookup = {}
        def dfs(node):
            if not node:
                return 
            if node in lookup:
                return lookup[node]
            clone = Node(node.val, []) # neighbors先设置为空数组
            lookup[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            return clone
        return dfs(node)
        