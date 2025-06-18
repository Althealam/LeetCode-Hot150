# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 前序遍历，判断left.left和right.right是否相同，以及left.right和right.left是否相同
# 也就是判断左子树的左子树和右子树的右子树，以及左子树的右子树和右子树的左子树是否是相同的
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.compare(root.left, root.right)
    
    def compare(self, left, right):
        if left is None or right is None:
            return left is right
        return left.val==right.val and self.compare(left.left, right.right) and self.compare(left.right, right.left)
        
        