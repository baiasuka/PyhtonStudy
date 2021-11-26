class BinaryNode:
    """
    二叉树节点对象
    """
    def __init__(self, value=None, lnode=None, rnode=None):
        self._value = value
        self._lnode = lnode
        self._rnode = rnode

    def get_value(self):
        return self._value
