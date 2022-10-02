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
    
    def render(self, current):
        self.matrix = GraphUtil.shift_left_matrix(self.matrix)
        scaled_to_index = round(GraphUtil.rescale(self.min, self.max, current)) - 1
        column = []
        for i in range(7, -1, -1):
            if i <= scaled_to_index:
                colour = GraphUtil.temp_colour(i, self.B, self.G, self.R)
                dot = colour
            else:
                dot = self.O
            column.append(dot)
        self.matrix = GraphUtil.set_column(self.matrix, 7, column)
        return GraphUtil.matrix_to_list(self.matrix)

