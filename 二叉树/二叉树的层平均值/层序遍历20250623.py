# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        queue = collections.deque([root])
        res = []
        while queue:
            size = len(queue)
            sum_ = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                sum_ += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(sum_/size)
        return res

        