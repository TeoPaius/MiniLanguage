import copy


class LLTable:
    def __init__(self, grammar):
        self.col_indices = copy.deepcopy(grammar.E + ['$'])
        self.row_indices = copy.deepcopy(grammar.E + grammar.N + ['$'])

        self.table = [['err' for _ in self.col_indices] for _ in self.row_indices]

    def get_indices(self, i, j):
        i = self.col_indices.index(i)
        j = self.col_indices.index(j)

        if i < 0:
            raise IndexError('\'{0}\' does not exist in the list'.format(i))

        if j < 0:
            raise IndexError('\'{0}\' does not exist in the list'.format(j))

        return i, j

    def set(self, i, j, val):
        i, j = self.get_indices(i, j)
        self.table[i][j] = val

    def get(self, i, j):
        i, j = self.get_indices(i, j)
        return self.table[i][j]

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.table)
