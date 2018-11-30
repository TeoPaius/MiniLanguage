import copy

from llparser.Grammar import Grammar


class LLParser:
    def __init__(self, filename):
        self.grammar = Grammar(filename)
        self.first = None
        self.follow = None

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
        f = {k: ([] if k != 'S' else ['ε']) for k in self.grammar.N}
        fp = {k: ([] if k != 'S' else ['ε']) for k in self.grammar.N}

        while self._compare_dicts(f, fp):
            for B in self.grammar.N:
                for production in self.grammar.P:
                    right = production[0]
                    left = production[1]
                    index = None

                    try:
                        index = left.index(B)
                    except ValueError:
                        pass

                    if index is not None and 0 < index < len(left) - 1:
                        y = left[index + 1]

                        if 'ε' in self.first[y]:
                            fp = f[B] + f[right]
                        else:
                            fp = f[B] + self.first[y]
            if self._compare_dicts(f, fp):
                break

            self.follow = copy.deepcopy(fp)

    def parse(self):
        self.create_first()
        self.create_follow()
        pass

    @staticmethod
    def _compare_dicts(dict1: dict, dict2: dict):
        for key in dict1.keys():
            if key not in dict2:
                return False

            if dict1[key] != dict2[key]:
                return False

        return True

    def create_table(self, first, follow, grammar):
        pass

    def analyse_seq(self, table, sequence):
        pass

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.grammar)
