
def list_to_matrix(l):
    c0 = []
    c1 = []
    c2 = []
    c3 = []
    c4 = []
    c5 = []
    c6 = []
    c7 = []
    for r in range(0, 64, 8):
        c0.append(l[r])
        c1.append(l[r+1])
        c2.append(l[r+2])
        c3.append(l[r+3])
        c4.append(l[r+4])
        c5.append(l[r+5])
        c6.append(l[r+6])
        c7.append(l[r+7])
    return [c0,c1,c2,c3,c4,c5,c6,c7]

def matrix_to_list(matrix):
    l = []
    for row in matrix:
        for e in row:
            l.append(e)
    return l

def rescale(minimum, maximum, m):
    if m <= minimum:
        return 1
    elif m >= maximum:
        return 8
    else:
        return ((m - minimum) / (maximum - minimum)) * ((8 - 1) + 1) # https://stats.stackexchange.com/questions/281162/scale-a-number-between-a-range
    
def shiftLeftMatrix(matrix):
    O = [0, 0, 0]  # Black
    tempColumn = [O, O, O, O, O, O, O, O]
    for row in matrix:
        for c in row:
            tempColour = tempColumn[c]
            tempColumn[c] = matrix[r+c]
            matrix[r+c] = tempColour
    return matrix

