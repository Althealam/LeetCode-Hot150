# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 思路：采用头插法，也就是从尾巴开始插入节点到链表中
# 右子树-左子树-根：DFS

# 时间复杂度：O(n)
# 空间复杂度：O(n)，递归需要O(n)的栈空间
class Solution:
    head = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return 
        self.flatten(root.right) # 右子树
        self.flatten(root.left) # 左子树
        # 中节点
        root.left=None
        root.right=self.head # 头插法
        self.head=root # 现在链表头节点为root
