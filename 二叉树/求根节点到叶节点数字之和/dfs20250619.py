# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 思路：从左边到右边，获取从根节点到叶子节点的数据，记录到res中

# 时间复杂度：O(n) 对每个节点访问一次
# 空间复杂度：O(n) 空间复杂度取决于递归调用栈的空间，递归栈的深度等于二叉树的高度，最坏情况下二叉树的高度等于节点个数
class Solution:
    def sumNumbers(self, root: Optional[TreeNode], x=0) -> int:
        def dfs(root, prevTotal):
            if not root:
                return 0
            total = prevTotal*10+root.val
            if not root.left and not root.right:
                return total
            else:
                return dfs(root.left, total)+dfs(root.right, total)
        return dfs(root, 0)