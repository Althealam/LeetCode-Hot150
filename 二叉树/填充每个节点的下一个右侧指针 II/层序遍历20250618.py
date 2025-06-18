"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# 思路：通过层序遍历来构造每个节点的右指针，定义一个prev来记录上一个节点

# 时间复杂度：O(n)
# 空间复杂度：O(h)，其中h是二叉树的高度，如果二叉树退化为链表的话则为n
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue=collections.deque([root])
        while queue:
            prev = None # 记录这一层的虚拟头节点
            for _ in range(len(queue)):
                node = queue.popleft()
                # 设置右之怎
                if prev is not None:
                    prev.next = node
                # 移动节点
                prev = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root

        