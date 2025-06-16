# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 思路：
# 1. 找到需要反转的链表的前一个节点值
# 2. 反转固定位置的链表

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 创建虚拟头节点（因为头节点也有可能被反转）
        dummy_head = ListNode(-1)
        dummy_head.next = head

        pre = dummy_head

        # 移动pre到left的前一个节点
        for _ in range(left-1):
            pre = pre.next
        
        # 反转区间
        cur = pre.next # 反转链表的起始节点
        for _ in range(right-left):
            # ========下面是重点部分========
            nxt = cur.next # 需要反转的起始节点的下一个节点
            # 取出next节点
            cur.next = nxt.next
            # nxt插入到pre后面
            nxt.next = pre.next
            # 更新pre的next指针
            pre.next = nxt
        return dummy_head.next 

            
