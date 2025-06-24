# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 思路：通过中序遍历获取二叉搜索树的数组，该数组为递增的，然后获取数组的第k个元素即可
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = self.inorder_traversal(root)
        return res[k-1]

    
    def inorder_traversal(self, root):
        res = []
        def dfs(root):
            if root.left:
                dfs(root.left)
            res.append(root.val)
            if root.right:
                dfs(root.right)
        dfs(root)
        return res
        