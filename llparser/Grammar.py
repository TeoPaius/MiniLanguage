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

                elif self.N is None:
                    self.N = line.split(',')
                    self.N.append(self.S)

                elif self.E is None:
                    self.E = line.split(',')

                else:
                    line = line.split('-')
                    self.P.append((line[0], [t for t in line[1].split(' ')]))

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "S: {0},\n" \
               "E: {1},\n" \
               "N: {2},\n" \
               "P: {3}" \
            .format(self.S, self.E, self.N, self.P)
