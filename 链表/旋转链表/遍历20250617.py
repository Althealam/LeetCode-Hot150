# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 思路：将链表每个节点向右移动k个位置，相当于将链表的后面k%len个节点移动到链表的最前面
# 步骤：
# 1. 求出链表长度
# 2. 找出倒数第k+1个节点
# 3. 链表重整：将链表的倒数第k+1个节点和倒数第k个节点断开，并将后半部分拼接到链表的头部

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 求出链表的长度
        length = self.get_list_length(head)

        # 找到倒数第K+1个节点
        if length == 0: # 避免出现除以0的情况出现
            return None

        k%=length # 对长度取模
        if k==0:
            return head
        fast, slow = head, head

        # 让fast先走k步
        for _ in range(k):
            fast = fast.next

        while fast.next:
            # slow指向倒数第k+1个节点前面的节点
            slow = slow.next
            fast = fast.next
        
        new_head = slow.next # 新链表的头
        slow.next = None
        fast.next=head

        return new_head

    def get_list_length(self, head):
        """求出链表的长度"""
        length = 0
        cur = head
        while cur:
            length+=1
            cur = cur.next
        return length

        


