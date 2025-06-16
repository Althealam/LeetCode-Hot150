"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# 题意：深拷贝一个链表，要求新链表中的每个节点都是新创建的，并且这些节点的random指针都指向新链表中的相应节点
# 复制普通链表：遍历链表，每轮建立新节点+构建前驱节点pre和当前节点node的引用指向
# 本题链表的节点新增了random指针，意味着在复制过程中，除了构建前驱节点和当前节点的引用指向pre.next之外，还要构建前驱节点和其随机节点的引用指向

# 思路：
# 1. 初始化头节点head为空节点，直接返回None
# 2. 初始化：哈希表dic，节点cur指向头节点
# 3. 复制链表
# （1）建立新节点，并向dic添加键值对（原cur节点，新cur节点）
# （2）cur遍历至原链表下一个节点
# 4. 构建新链表的引用指向
# （1）构建新节点的next和random引用指向
# （2）cur遍历至原链表的下一个节点
# 5. 返回值：新链表的头节点dic[cur]

# 时间复杂度：O(N)，两轮遍历链表
# 空间复杂度：O(N)，哈希表dic使用线性大小的额外空间
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        dic = {} # 哈希表

        # 1. 创建所有新节点，建立原节点到新节点的映射
        # 复制各个节点，建立“原节点->新节点”的map映射
        cur = head
        while cur:
            dic[cur]=Node(cur.val) # 创建新节点并存储映射
            cur=cur.next

        # 2. 利用已建立的映射，设置新节点的指针关系
        # 构建新节点的next和random指向
        cur=head
        while cur:
            dic[cur].next=dic.get(cur.next) # 设置新节点的next指针
            dic[cur].random=dic.get(cur.random) # 设置新节点的random指针
            cur = cur.next
        # 返回新链表的头节点
        return dic[head]
        