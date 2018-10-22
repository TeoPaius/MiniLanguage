from model.Pif import Pif
from model.SymbolTable import SymbolTable
from rules import rules


class Parser:
    def __init__(self):
        pass

    @staticmethod
    def parseFile(fileName):
        pif = Pif()
        st = SymbolTable()
        buffer = ""

        with open(fileName) as file:
            while True:
                c = file.read(1)
                if not c:
                    break

                if c == '\n':
                    continue

                if c in rules.separators or c in rules.operators:
                    if buffer != "":
                        print(buffer)
                        Parser.processToken(buffer, pif, st)

                    if c != ' ':
                        print(c)
                    buffer = ""
                else:
                    buffer += c

        return pif, st

    @staticmethod
    def processToken(token, pif, st):
        if token in rules.keywords or token in rules.operators or token in rules.separators :
            pif.pif.append((rules.codes[token], -1))
        else:
            if Parser.isConstant(token):
                id = st.add(token)
                pif.pif.append(0, id)

            if Parser.isIdentifier(token):
                id = st.add(token)
                pif.pif.append(1, id)




    @staticmethod
    def isConstant(token):
        pass

    @staticmethod
    def isIdentifier(token):
        pass