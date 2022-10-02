import GraphUtil


class Graph:
    def __init__(self, minimum, maximum):
        self.min = minimum
        self.max = maximum
        self.R = [255, 0, 0]  # Red
        self.G = [0, 255, 0]  # Green
        self.B = [0, 0, 255]  # Blue
        self.O = [0, 0, 0]  # Black
        O = self.O
        self.matrix = GraphUtil.list_to_matrix([
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O
            ])
    
    def __colour(self, row_index):
        colour = self.B
        if row_index < 2 * 8:
            colour = self.R
        elif row_index < 6 * 8:
            colour = self.G
        return colour
    
    def render(self, current):
        self.matrix = GraphUtil.shift_left_matrix(self.matrix)
        scaled = round(GraphUtil.rescale(self.min, self.max, current))
        column = []
        for i in range(0, 8):
            if i <= scaled:
                colour = self.__colour(i)
                dot = colour
            else:
                dot = self.O
            column.append(dot)
        self.matrix = GraphUtil.set_column(self.matrix, 7, column)
        return GraphUtil.matrix_to_list(self.matrix)
#         print("scaled:" + str(scaled))
#         for r in range(56, (7 - scaled) * 8, -8):
#             colour = self.__colour(r)
#             self.matrix[r] = colour
#         return self.matrix


