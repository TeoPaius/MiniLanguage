from llparser.Grammar import Grammar


class LLParser:
    def __init__(self, filename):
        self.grammar = Grammar(filename)
        self.first = None

    def create_first(self):
        res = {}
        for i in self.grammar.N:
            res[i] = []

        for terminal in self.grammar.E:
            res[terminal] = [terminal]

        i = 0
        for prod in self.grammar.P:
            if prod.right[0] in self.grammar.E:
                res[prod.left][i] = prod.right[0]

        self.first = {'S': ['(', 'a'], 'A': ['+', 'ε'], 'C': ['ε', '+'], 'D': ['(', 'a'], 'B': ['(', 'a']}

    def create_follow(self):
        f = {k: ([] if k != 'S' else ['ε']) for k in self.grammar.N}
        fp = {k: ([] if k != 'S' else ['ε']) for k in self.grammar.N}

        while self._compare_dicts(f, fp):
            for B in self.grammar.N:
                for A in self.grammar.P:
                    A = A[1]
                    if B in A and 0 < A.index(B) < len(A) - 1:
                        print(B)
            if fp == f:
                break

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
