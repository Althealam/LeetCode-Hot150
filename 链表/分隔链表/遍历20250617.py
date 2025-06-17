# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 思路：建立两个新的链表来实现原链表的分割
# 1. 定义cur遍历链表，如果cur的值小于x那么将其接入到第一个链表里，否则接入到第二个链表里
# 2. 将两个链表拼接起来

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small_dummy_node = ListNode(0)
        big_dummy_node = ListNode(0)
        small = small_dummy_node
        big = big_dummy_node
        # 遍历链表判断其节点值
        while head:
            if head.val<x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            head = head.next
        # 将两个链表连接起来
        small.next = big_dummy_node.next
        big.next = None
        return small_dummy_node.next


        