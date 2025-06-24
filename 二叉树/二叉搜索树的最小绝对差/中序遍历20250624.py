# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 思路：通过中序遍历获取二叉搜索树的数组，然后计算两两节点之间的差，选择最小的作为两值之差的最小值
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = self.inorder_traversal(root) # 获取中序遍历的数组
        ans = float('inf')
        for i in range(1, len(res)):
            ans = min(ans, res[i]-res[i-1])
        return ans
    
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
        