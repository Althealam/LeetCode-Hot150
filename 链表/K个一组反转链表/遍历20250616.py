# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. 求出链表个数，每次反转前判断剩余个数：如果剩余个数>=k则反转；如果剩余个数<k则不能反转
        n=0
        cur = head
        while cur:
            n+=1
            cur = cur.next

        # 2. 反转链表
        dummy_node = ListNode(next=head)  # 虚拟头节点
        p0=dummy_node
        while n>=k: # 判断剩余的节点是否满足反转条件
            n-=k # 减去k个元素
            pre = None # 当前反转的链表的上一个节点
            cur=p0.next # 当前正在遍历的节点

            # 反转k个节点（反转操作次数为k-1）
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre=cur
                cur=nxt
            
            # 临时变量nxt保存下一段要反转的链表的起始节点
            nxt=p0.next
            # 将反转后的链表和左边的部分连接起来
            p0.next.next=cur
            # 将反转后的链表和右边的部分连接起来
            p0.next=pre
            # 更新p0的值，将p0更新成下一段要反转的链表的上一个节点
            p0=nxt
        return dummy_node.next