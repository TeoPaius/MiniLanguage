from llparser.Grammar import Grammar


class LLParser:
    def __init__(self, filename):
        self.grammar = Grammar(filename)

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

    def create_follow(self, first, grammar):
        pass

    def create_table(self, first, follow, grammar):
        pass

    def analyse_seq(self, table, sequence):
        pass

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.grammar)
