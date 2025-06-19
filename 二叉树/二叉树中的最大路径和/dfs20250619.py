# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 思路：
# 空节点的最大贡献值为0
# 非空节点的最大贡献值等于节点值与其子节点的最大贡献值之和（对于叶子节点而言，其最大贡献值等于节点值，相当于子节点的贡献值为0）
# dfs用于获取每个节点的最大贡献值，而ans为最大路径和，取决于该节点的值和该节点的左右子节点的最大贡献值

# 时间复杂度：O(n)，其中n是二叉树的节点个数
# 空间复杂度：O(N)，空间复杂度取决于递归调用层数，最大层数等于二叉树的高度，最坏情况下二叉树的高度等于二叉树中的节点个数

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf') # 二叉树中的最大路径和
        def dfs(node):
            """获取每个节点的最大贡献值"""
            if node is None:
                return 0 # 没有节点，和为0
            
            # 计算左右子节点的贡献值
            left_val = max(dfs(node.left), 0)
            right_val = max(dfs(node.right), 0)

            # 计算和
            val = node.val+left_val+right_val

            # 更新答案值
            nonlocal ans
            ans = max(ans, val)
        
            return max(left_val, right_val)+node.val
        dfs(root)
        return ans