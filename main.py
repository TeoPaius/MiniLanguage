from llparser.Grammar import Grammar
from llparser.LLParser import LLParser
from model.Parser import Parser
from binaryTree.tree import Tree

if __name__ == '__main__':
    # p = Parser()

    # pif, st = Parser.parseFile("input.in")
    #
    #
    # print("--PIF--\n"+ str(pif) + "\n--PIF--\n")
    # print("--ST--\n" + str(st) + "\n--ST--\n")

    #
    # tree = Tree()
    #
    # print(tree.add("5"))
    # print(tree.add("3"))
    # print(tree.add("1"))
    # print(tree.add("9"))
    # print(tree.add("8"))
    # print(tree.add("7"))
    # # print(tree.add("1"))
    #
    # print("\n")
    #
    # for node in tree.inorder():
    #     print(node)

    llparser = LLParser('llparser/gramm.ar')

    # print(llparser)
    llparser.parse()

    print(llparser.follow)
