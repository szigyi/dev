

def list_to_matrix(list_of_m):
    #    0   1   2   3   4   5   6   7
    m = [[], [], [], [], [], [], [], []]
    for r in range(0, 8):
        temp_array = []
        for c in range(0, 8):
            if r == 0:
                index = c
            else:
                index = r * 8 + c
            temp_array.append(list_of_m[index])
        m[r] = temp_array
    return m


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


def set_column(matrix, column_index, column):
    for r in range(0, len(matrix)):
        matrix[r][column_index] = column[r]
    return matrix

def shift_left_matrix(matrix):
    o = [0, 0, 0]  # Black
    for r in range(0, len(matrix)):
        matrix[r] = __shift_array(matrix[r], o)
    return matrix


def __shift_array(array, default):
    size = len(array)
    for i in range(0, size):
        if i == size - 1:
            temp = default
        else:
            temp = array[i+1]
        array[i] = temp
    return array

