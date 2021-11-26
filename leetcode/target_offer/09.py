# 剑指 Offer 09. 用两个栈实现队列
# 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )
#
# 示例 1：
#
# 输入：
# ["CQueue","appendTail","deleteHead","deleteHead"]
# [[],[3],[],[]]
# 输出：[null,null,3,-1]
# 示例 2：
#
# 输入：
# ["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
# [[],[],[5],[2],[],[]]
# 输出：[null,-1,null,null,5,2]
from collections import deque


class CQueue:
    def __init__(self):
        self.stack_in = deque()
        self.stack_out = deque()
        self.status = 0

    def appendTail(self, value: int) -> None:
        if self.status == 0:
            self.stack_in.append(value)
        elif self.status == 1:
            self.stack_in.append(value)
        else:
            while self.stack_out:
                self.stack_in.append(self.stack_out.pop())
            self.stack_in.append(value)
        self.status = 1

    def deleteHead(self) -> int:
        if self.status == 0:
            return -1
        elif self.status == 1:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            self.status = 2
            return self.stack_out.pop()
        else:
            if self.stack_out:
                self.status = 2
                return self.stack_out.pop()
            else:
                self.status = 2
                return -1


tq = CQueue()
print(tq.deleteHead())
tq.appendTail(5)
tq.appendTail(2)
print(tq.deleteHead())
tq.appendTail(6)
print(tq.deleteHead())
print(tq.deleteHead())
print(tq.deleteHead())
