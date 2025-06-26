# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 思路：
# 1. 先将链表从中间节点断开
# 2. 合并两个有序链表（注意需要建立虚拟头节点）
# 3. 返回最终合并后的链表

# 时间复杂度：O(nlogn)
# 空间复杂度：O(logn)
class Solution:
    def middleNode(self, head):
        """使用快慢指针分离一个链表"""
        slow = fast = head
        # fast比slow快一个节点
        while fast and fast.next:
            pre = slow # 记录slow前面的一个节点
            slow = slow.next
            fast = fast.next.next 
        pre.next = None # 断开slow的前一个节点和slow的连接
        return slow 

    def mergeTwoLists(self, list1, list2):
        """合并两个有序链表"""
        dummy_head = ListNode()
        cur = dummy_head
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        # 处理剩余节点
        cur.next = list1 if list1 else list2
        return dummy_head.next
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        # 找到中间节点head2，并断开head2与前面一个节点的连接
        head2 = self.middleNode(head)
        # 分治
        head = self.sortList(head)
        head2 = self.sortList(head2)
        # 合并
        return self.mergeTwoLists(head, head2)

        

        