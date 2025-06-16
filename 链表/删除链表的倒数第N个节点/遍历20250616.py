# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 思路：定义双指针fast和slow，然后让fast先走n步，slow和fast同步移动节点，当fast到达最后一个节点时，slow就到达了倒数第n个节点
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(next=head)
        slow, fast = dummy_node, dummy_node
        for _ in range(n+1):
            fast = fast.next
        # 此时fast走了n步
        while fast: # 当fast到达最后一个节点的时候，slow到达要删除的节点的前面一个节点
            slow = slow.next
            fast = fast.next
        # 此时slow指向了倒数第N个节点的前面一个节点
        tmp = slow.next.next
        slow.next = tmp
        return dummy_node.next