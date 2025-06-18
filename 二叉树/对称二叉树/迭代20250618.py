# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 迭代法：用栈存储每一层的节点，然后判断节点的左右孩子节点的情况
# 时间复杂度：O(n)
# 空间复杂度：O(h)其中h为二叉树的高度，如果二叉树退化为链表的话h为n

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack=[(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if left is None and right is not None:
                return False
            if left is not None and right is None:
                return False
            if left is not None and right is not None:
                if left.val!=right.val:
                    return False
                else:
                    stack.append((left.left, right.right))
                    stack.append((left.right, right.left))
        return True