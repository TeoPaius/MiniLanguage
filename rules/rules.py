separators = ['(', ')', '[', ']', '{', '}', ' ', '|', '\n', ';']
keywords = [" ", "main", "char", "array", "const", "else", "if", "int", "while", "write", "true", "false", "cin",
            "cout", "string", "bool", "char", "struct"]
operators = ["+", "-", "*", "/", "!=", "=", "<", ">", "<=", "==", ">=", "(", ")", "[", "]", "{", "}", "|", "_"]

identifierRegEx = "^[^\d][a-zA-Z0-9]{0,254}"  # matches words that dont start with digit and then 254 other letters(upper and lower case) or digits
numberRegEx = "([-]?[1-9][0-9]*)|[0]"  # matches numbers that start with a - optionally follwed by one non zero digit and then as many other digits
stringRegEx = "\"\w*\""  # matches a sequence of writable chars ecapsulated by double quotes
charRegEx = "\'\w?\'"  # matches a characted ecapsulated by single quotes

codes = {list(set(separators + keywords + operators))[i]: i + 2 for i in
         range(0, len(set(separators + keywords + operators)))}
# codes = {"main": 2,
#          "struct": 3,
#          "const": 4,
#          "int": 5,
#          "char": 6,
#          "bool": 7,
#          "string": 8,
#          "___": 9,
#          "___": 10,
#          "if": 11,
#          "else": 12,
#          "while": 13,
#          "cin": 14,
#          "cout": 15,
#          "{": 16,
#          "}": 17,
#          "[": 18,
#          "]": 19,
#          "(": 20,
#          ")": 21,
#          "+": 22,
#          "-": 23,
#          "*": 24,
#          "/": 25,
#          "<": 26,
#          "<=": 27,
#          "==": 28,
#          "!=": 29,
#          ">=": 30,
#          ">": 31,
#          "=": 32,
#          " ": 33,
#          ";": 34}
