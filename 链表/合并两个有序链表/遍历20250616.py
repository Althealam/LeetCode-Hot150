# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 思路：定义两个指针idx_1和idx_2，分别指向两个链表的节点，将较小的节点值添加到结果里
# 时间复杂度：O(n+m)
# 空间复杂度：O(1)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-1) # 创建一个虚拟节点

        nxt = dummy_head
        while list1 and list2: # 遍历两个链表并且两个链表都不为空
            if list1.val<=list2.val: # 比较两个节点值，将较小的节点值插入进去
                nxt.next = list1
                list1 = list1.next
            elif list1.val>list2.val:
                nxt.next = list2
                list2 = list2.next
            
            # 移动节点值
            nxt = nxt.next
        
        # 此时有一个链表为空了
        nxt.next = list1 if list1 is not None else list2
        return dummy_head.next

        