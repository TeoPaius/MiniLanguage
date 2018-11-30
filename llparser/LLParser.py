from llparser.Grammar import Grammar


class LLParser:
    def __init__(self, filename):
        self.grammar = Grammar(filename)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.grammar)
