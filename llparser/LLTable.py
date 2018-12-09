import copy


class LLTable:
    def __init__(self, grammar):
        self.col_indices = copy.deepcopy(grammar.E + ['$'])
        self.row_indices = copy.deepcopy(grammar.E + grammar.N + ['$'])

        # Create the table
        self.table = [['err' for _ in self.col_indices] for _ in self.row_indices]

        # Put pop for non terminals
        for non_terminal in grammar.E:
            self.set(non_terminal, non_terminal, 'pop')

        # Put acc for $ $
        self.set('$', '$', 'acc')

    def get_indices(self, i, j):
        i = self.row_indices.index(i)
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
        # Format header
        string = "-\t"
        for item in self.col_indices:
            string += '\t{0}'.format(item)
        string += '\n'

        # Format each line
        for i in range(0, len(self.table)):
            string += '{0}\t'.format(self.row_indices[i])

            for j in range(0, len(self.table[i])):
                string += '{0}\t'.format(self.table[i][j])

            string += '\n'

        return string
