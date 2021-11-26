from data_structures.tree import BinaryNode

class BinarySortTreeNode(BinaryNode):
    """
    二叉排序树节点对象
    """
    def __init__(self, value):
        if isinstance(value, int):
            self._value = value
            self._lnode = None
            self._rnode =None
        else:
            raise TypeError

    def insert_value(self, new_value):
        """
        插入新值，若大于当前节点的值放入右子节点，小于当前节点的值则放入左子节点,相等则抛出异常
        :param new_value:
        :return:
        """
        new_node = BinarySortTreeNode(new_value)
        if new_value > self._value:
            self._rnode = new_node
        elif new_value < self._value:
            self._lnode = new_node
        else:
            raise ValueError


class BinarySortTree:
    """
    二叉排序树
    """
    def __init__(self, value):
        self._root = BinarySortTreeNode(value)
        self._depth = 1
        self._values = [value]

    def get_values(self):
        return self._values

    def search_value(self, target_value):
        current_node = self._root
        while 1:


    def insert_value(self, new_value):
        if new_value in self._values:
            return False
        else:
            new_node = BinarySortTreeNode(new_value)
            target_node = self._root

            self._values.append(new_value)



if __name__ == '__main__':
    tree = BinarySortTree(1)

