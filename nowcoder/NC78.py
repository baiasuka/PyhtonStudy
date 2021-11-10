# 单链表反转，
# 数据范围： leq1000n≤1000
# 要求：空间复杂度 O(1) ，时间复杂度 O(n) 。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def ReverseListByStack(self, head: ListNode) -> ListNode:
        """
        使用栈的方法，先进后出重新构建链表
        :param head:
        :return:
        """
        if not head:
            return None
        temp_stack = []
        while head != None:
            temp_stack.append(head.val)
            head = head.next

        new_head = ListNode(temp_stack.pop())
        tail = new_head
        while temp_stack:
            new_node = ListNode(temp_stack.pop())
            tail.next = new_node
            tail = tail.next
        return new_head



