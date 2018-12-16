from binaryTree.tree import Tree


class SymbolTable:
    def __init__(self):
        self.st = Tree()

    def add(self, token):
        return self.st.add(token)

    def getSybmols(self):
        return [i.data for i in self.st.inorder()]

    def __str__(self):
        return ','.join([str(i) for i in self.st.inorder()])
