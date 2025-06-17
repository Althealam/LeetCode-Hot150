# 前序遍历：中左右==先判断中节点是否相同，再判断左右子树的节点是否相同
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is not None and q is None:
            return False
        elif p is None and q is not None:
            return False
        elif p.val!=q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        