# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 思路：从左边到右边，获取从根节点到叶子节点的数据，记录到res中

# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def sumNumbers(self, root: Optional[TreeNode], x=0) -> int:
        if root is None:
            return 0
        x=x*10+root.val # 计算这条路径的和
        if root.left is None and root.right is None: # 叶子节点
            return x
        return self.sumNumbers(root.left, x)+self.sumNumbers(root.right, x)