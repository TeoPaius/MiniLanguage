import copy

from llparser.Grammar import Grammar
from llparser.LLTable import LLTable


class LLParser:
    def __init__(self, filename):
        self.grammar = Grammar(filename)
        self.first = None
        self.follow = None
        self.table = None

    def create_first(self):
        res = {}
        maxI = 10
        for i in self.grammar.N:
            res[i] = [[] for _ in range(0, maxI)]

        for terminal in self.grammar.E:
            res[terminal] = [[terminal] for _ in range(0, maxI)]

        for prod in self.grammar.P:
            if prod[1][0] in self.grammar.E:
                res[prod[0]][0] += ([prod[1][0]])

        i = 0
        ok = False
        while not ok:
            i = i + 1
            for x in self.grammar.N:
                res[x][i] += res[x][i - 1]
                for prod in self.grammar.P:
                    if prod[0] == x:
                        res[x][i] += res[prod[1][0]][i - 1]
                        res[x][i] = list(set(res[x][i]))
            ok = True
            for x in res.keys():
                if res[x][i - 1] != res[x][i]:
                    ok = False

        self.first = {}
        for k in res.keys():
            self.first[k] = res[k][i]

    def create_follow(self):
        f = {k: (set() if k != 'S' else set('ε')) for k in self.grammar.N}
        modified = True

        while modified:
            modified = False

            for B in self.grammar.N:
                for production in self.grammar.P:
                    tempfb = copy.deepcopy(f[B])

                    left = production[0]
                    right = production[1]
                    index = None

                    try:
                        index = right.index(B)
                    except ValueError:
                        pass

                    if index is not None and 0 < index < len(right) - 1:
                        y = right[index + 1]

                        f[B].update(set(self.first[y]))

                        if 'ε' in self.first[y]:
                            f[B].remove('ε')
                            f[B].update(set(f[left]))

                    elif index is not None and index == len(right) - 1:
                        f[B].update(set(f[left]))

                    if f[B] != tempfb:
                        modified = True

            if not modified:
                break

        self.follow = copy.deepcopy(f)

    def parse(self):
        self.create_first()
        self.create_follow()
        self.create_table()
        pass

    @staticmethod
    def _compare_dicts(dict1: dict, dict2: dict):
        for key in dict1.keys():
            if key not in dict2:
                return False

            if dict1[key] != dict2[key]:
                return False

        return True

    def create_table(self):
        self.table = LLTable(self.grammar)

        for i in range(0, len(self.grammar.P)):
            first = self.first[self.grammar.P[i][1][0]]
            if 'ε' not in first:
                for elem in first:
                    self.table.set(self.grammar.P[i][0], elem, (self.grammar.P[i][1], i))
            else:
                for elem in self.follow[self.grammar.P[i][0]]:
                    self.table.set(self.grammar.P[i][0], elem, (self.grammar.P[i][1], i))

        print(self.table)

    def analyse_seq(self, table, sequence):
        pass

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.grammar)
