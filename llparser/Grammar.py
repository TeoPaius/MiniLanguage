class Grammar:
    def __init__(self, filename):
        self.__filename = filename

        self.S = None
        self.E = None
        self.N = None
        self.P = []

        self.__read_from_file()

    def __read_from_file(self):
        with open(self.__filename, 'r') as file:
            for line in file:
                line = line.strip('\n')

                if self.S is None:
                    self.S = line

                elif self.E is None:
                    self.E = line.split(',')

                elif self.N is None:
                    self.N = line.split(',')

                else:
                    line = line.split('-')
                    self.P.append((line[0], [char for char in line[1]]))

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "S: {0},\n" \
               "E: {1},\n" \
               "N: {2},\n" \
               "P: {3}" \
            .format(self.S, self.E, self.N, self.P)
