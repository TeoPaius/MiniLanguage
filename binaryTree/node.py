class Node:
    def __init__(self, data, left, right, idx):
        self.data = data
        self.left = left
        self.right = right
        self.idx = idx

    def __str__(self):
        return self.data