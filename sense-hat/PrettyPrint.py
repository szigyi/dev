
def prettyPrint(matrix):
    for row in matrix:
        line = ""
        for c in row:
            line += str(c)
            line += ", "
        print(line)