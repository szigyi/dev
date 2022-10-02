import GraphUtil


class Graph:
    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.R = [255, 0, 0]  # Red
        self.G = [0, 255, 0]  # Green
        self.B = [0, 0, 255]  # Blue
        self.O = [0, 0, 0]  # Black
        O = self.O
        self.matrix = [
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O
            ]
    
    def __colour(self, rowIndex):
        colour = self.B
        if rowIndex < 2 * 8:
            colour = self.R
        elif rowIndex < 6 * 8:
            colour = self.G
        return colour
    
    def render(self, current):
        scaled = round(GraphUtil.rescale(self.min, self.max, current))
#         print("scaled:" + str(scaled))
        for r in range(56, (7 - scaled) * 8, -8):
            colour = self.__colour(r)
            self.matrix[r] = colour
        return self.matrix


