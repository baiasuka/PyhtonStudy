# 21.合并有序链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        遍历l1和l2，期间比对出val较小的node放入结果链表
        :param l1:
        :param l2:
        :return:
        """
        head_node = ListNode(0)
        tail_node = head_node

        while l1 and l2:
            if l1.val <= l2.val:
                new_node = ListNode(l1.val)
                l1 = l1.next
            else:
                new_node = ListNode(l2.val)
                l2 = l2.next
            tail_node.next = new_node
            tail_node = tail_node.next
        if l1 and not l2:
            tail_node.next = l1
        elif l2 and not l1:
            tail_node.next = l2
        head_node = head_node.next
        return head_node


if __name__ == '__main__':
    l1 = ListNode(1)
    l1_head = l1
    for i in [2,4]:
        n_node = ListNode(i)
        l1.next = n_node
        l1 = l1.next
    l2 = ListNode(1)
    l2_head = l2
    for j in [3,4]:
        n_node = ListNode(j)
        l2.next = n_node
        l2 = l2.next
    fl = Solution().mergeTwoLists(l1_head, l2_head)
    while fl:
        print(fl.val)
        fl = fl.next
