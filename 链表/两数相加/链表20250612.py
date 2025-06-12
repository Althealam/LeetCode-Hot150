# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 思路：获取两个链表的节点值val1和val2，然后和进位值相加，除以10的余数就是当前节点需要保存的数位
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        if l1 is None and l2 is None and carry==0: # 递归边界
            return None
        s=carry # 进位值
        if l1: # l1链表不为空
            s+=l1.val # 累加进位值和节点值
            l1=l1.next # 获取下一个节点值
        if l2: # l2链表不为空
            s+=l2.val # 累加进位值
            l2=l2.next
        
        # s除以10的余数为当前节点值，商为进位
        return ListNode(s%10,self.addTwoNumbers(l1, l2, s//10))
        

        