from binaryTree.node import *


class Tree:
    def __init__(self):
        self.root = None
        self.nrNodes = 0

    def add(self, data):

        node = Node(data, None, None, self.nrNodes)
        self.nrNodes += 1
        if self.root is None:
            self.root = node
            return 0

        return self._addInternal(self.root, node)

    def _addInternal(self, targetNode, sourceNode):
        if targetNode.data > sourceNode.data:
            if targetNode.left is None:
                targetNode.left = sourceNode
                return 0
            else:
                return self._addInternal(targetNode.left, sourceNode)
        if targetNode.data <= sourceNode.data:
            if targetNode.right is None:
                targetNode.right = sourceNode
                return 1
            else:
                return 1 + self._addInternal(targetNode.right, sourceNode)

    def inorder(self):
        for i in self._inoderInternal(self.root):
            yield i

    def _inoderInternal(self, node):
        if node is None:
            return

        for i in self._inoderInternal(node.left):
            yield i
        yield node
        for i in self._inoderInternal(node.right):
            yield i
