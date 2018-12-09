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
        print(self.follow)

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


    def split_seq(self, seq):
        return seq.split(' ')


    def analyse_seq(self, sequence):

        working_stack = ['$', self.grammar.S]
        input_stack = ['$'] + sequence
        output = []

        while True:
            u = input_stack[-1]
            A = working_stack[-1]

            if self.table.get(A,u) == "err":
                print("ERROR PARSING" + '\nw_stack: ' + str(working_stack) + "\ni_stack: " + str(input_stack))
                return None
            if self.table.get(A,u) == "acc":
                print("OK PARSING")
                return output
            if self.table.get(A,u) == "pop":
                input_stack.pop()
                working_stack.pop()
                continue

            B = self.table.get(A,u)[0]
            i = self.table.get(A,u)[1]

            working_stack.pop()
            for idx in range(len(B)-1, -1, -1):
                working_stack.append(B[idx])
            output.append(i)



    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.grammar)
