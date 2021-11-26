# 100.相同的树

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def preOrderTraversal(root_node):
            """
            使用栈来记录节点实现先序遍历，当左孩子不存在时
            :return:
            """
            stack = []
            pre_order_list = []
            treeNode = root_node
            while treeNode or stack != []:
                while treeNode != None:
                    pre_order_list.append(treeNode.val)
                    stack.append(treeNode)
                    treeNode = treeNode.left
                if stack != []:
                    treeNode = stack.pop()
                    treeNode = treeNode.right
            return pre_order_list

        firstL = preOrderTraversal(p)
        secondeL = preOrderTraversal(q)
        if firstL == secondeL:
            return True
        else:
            return False