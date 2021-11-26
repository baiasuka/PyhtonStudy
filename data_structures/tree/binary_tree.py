class BinaryNode:
    """
    二叉树节点对象
    """
    def __init__(self, value=None, lnode=None, rnode=None):
        self.value = value
        self.lnode = lnode
        self.rnode = rnode

    def get_value(self):
        """
        获取节点的值
        :return:
        """
        return self.value

    def insert_left_node(self, value):
        """
        在左侧插入新节点，返回新节点
        :return:
        """
        new_node = BinaryNode(value)
        if self.lnode:
            return False
        else:
            self.lnode = new_node
            return new_node

    def insert_right_node(self, value):
        """
        在右侧插入新节点，返回新节点
        :param value:
        :return:
        """
        new_node = BinaryNode(value)
        if self.rnode:
            return False
        else:
            self.rnode = new_node
            return new_node


class BinaryTree:
    def __init__(self, root_node):
        self._root_node = root_node

    def preOrderTraversal(self):
        """
        使用栈来记录节点实现先序遍历，当左孩子不存在时访问右孩子
        :return:
        """
        stack = []
        pre_order_list = []
        treeNode = self._root_node
        while treeNode or stack != []:
            while treeNode != None:
                pre_order_list.append(treeNode.get_value())
                stack.append(treeNode)
                treeNode = treeNode.lnode
            if stack != []:
                treeNode = stack.pop()
                treeNode = treeNode.rnode
        return pre_order_list

    def midOrderTraversal(self):
        stack = []
        pre_order_list = []
        treeNode = self._root_node
        while treeNode or stack != []:
            while treeNode != None:
                pre_order_list.append(treeNode.get_value())
                stack.append(treeNode)
                treeNode = treeNode.lnode
            if stack != []:
                treeNode = stack.pop()
                treeNode = treeNode.rnode

if __name__ == '__main__':
    root_node = BinaryNode(1)
    root_node.lnode = BinaryNode(2)
    root_node.rnode = BinaryNode(3)
    tree = BinaryTree(root_node)
    print(tree.preOrderTraversal())

