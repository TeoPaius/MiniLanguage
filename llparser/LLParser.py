class LLParser:
    def __init__(self):
        pass


    def createFirst(self, grammar):
        res = {}
        for i in grammar.N:
            res[i] = []

        for terminal in grammar.E:
            res[terminal] = [terminal]

        i = 0
        for prod in grammar.P:
            if prod.right[0] in grammar.E:
                res[prod.left][i] = prod.right[0]


    def createFollow(self, first, grammar):
        pass

    def createTable(self, first, follow, grammar):
        pass

    def analyseSeq(self, table, sequence):
        pass
