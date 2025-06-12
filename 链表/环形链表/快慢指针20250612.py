# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路：定义快慢指针，如果有环，那么快慢指针会相遇
# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=fast=head # 让快慢指针同时在head出发
        while fast and fast.next:
            slow=slow.next # 慢指针走一步
            fast=fast.next.next # 快指针走两步
            if fast == slow: # 快慢指针相遇
                return True
        return False # 快指针访问到链表末尾，但是一直没有相遇

        