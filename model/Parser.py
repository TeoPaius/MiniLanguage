from model.Pif import Pif
from model.SymbolTable import SymbolTable
from rules import rules
import re
import sys

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
                    if c == '<' or c == '>' or c == '=':
                        pos = file.tell()
                        nextChar = file.read(1)
                        if nextChar == '=':
                            c+= nextChar
                        else:
                            file.seek(pos)

                    if buffer != "":
                        Parser.processToken(buffer, pif, st)

                    if c != ' ':
                        Parser.processToken(c, pif, st)

                    buffer = ""
                else:
                    buffer += c

        Parser.processToken(buffer, pif, st)
        return pif, st

    @staticmethod
    def processToken(token, pif, st):
        print(token)
        if token in rules.keywords or token in rules.operators or token in rules.separators :
            pif.pif.append((rules.codes[token], -1))
        else:
            oldSt = st.getSybmols()



            if Parser.isConstant(token):
                if token in oldSt:
                    pif.pif.append((0, oldSt.index(token)))
                else:
                    idx = st.add(token)
                    pif.pif.append((0, -4))
                    Parser.reorganizePif(pif, oldSt, st.getSybmols())
                return

            if Parser.isIdentifier(token):
                if token in oldSt:
                    pif.pif.append((1, oldSt.index(token)))
                else:
                    idx = st.add(token)
                    pif.pif.append((1, -4))
                    Parser.reorganizePif(pif, oldSt, st.getSybmols())
                return

            sys.exit("ERROR AT TOKEN: " + token)


    @staticmethod
    def reorganizePif(pif, oldSt, newSt):
        idx = -1

        for i in range (0, len(oldSt)):
            if oldSt[i] != newSt[i]:
                idx = i
                break
        if idx == -1:
            idx = len(newSt) -1


        for i in range(0, len(pif.pif) - 1):
            if pif.pif[i][1] == -1:
                continue
            else:
                if pif.pif[i][1] >= idx:
                    pif.pif[i] = (pif.pif[i][0],pif.pif[i][1] + 1)

        pif.pif[len(pif.pif)-1] = (pif.pif[len(pif.pif)-1][0], idx)




    @staticmethod
    def isStringConstant(token):
        if re.fullmatch(rules.stringRegEx, token) is None:
            return False
        return True

    @staticmethod
    def isNumberConstant(token):
        if re.fullmatch(rules.numberRegEx, token) is None:
            return False
        return True

    @staticmethod
    def isCharConstant(token):
        if re.fullmatch(rules.charRegEx, token) is None:
            return False
        return True

    @staticmethod
    def isConstant(token):
        if Parser.isNumberConstant(token) or Parser.isStringConstant(token) or Parser.isCharConstant(token):
            return True
        return False

    @staticmethod
    def isIdentifier(token):
        if re.fullmatch(rules.identifierRegEx, token) is None:
            return False
        return True