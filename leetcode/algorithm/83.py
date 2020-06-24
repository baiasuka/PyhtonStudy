# 83.删除排序链表中的重复元素

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head:
            if head.next == None:
                return head
            else:
                pre = head
                tail = head.next
                while tail:
                    if tail.val == pre.val:
                        tail = tail.next
                        pre.next = tail
                    else:
                        tail = tail.next
                        pre = pre.next
                return head
        else:
            return False

if __name__ == '__main__':
    tl = ListNode(1)
    buf = tl
    for i in [1,2,3,3,4,4,4,5,5]:
        nn = ListNode(i)
        buf.next = nn
        buf = nn

    nl = Solution().deleteDuplicates(tl)
    while nl.next:
        print(nl.val)
        nl = nl.next
    print(nl.val)

