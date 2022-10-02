import GraphUtil
import PrettyPrint

def should_rescale_less_than_min():
    result = GraphUtil.rescale(10, 20, 2)
    print(result)
    assert result == 1, "should_rescale_less_than_min"

def should_rescale_more_than_max():
    result = GraphUtil.rescale(10, 20, 25)
    print(result)
    assert result == 8, "should_rescale_more_than_max"

def should_rescale_min():
    result = GraphUtil.rescale(10, 20, 10)
    print(result)
    assert result == 1, "should_rescale_min"

def should_rescale_max():
    result = GraphUtil.rescale(10, 20, 20)
    print(result)
    assert result == 8, "should_rescale_max"

def should_rescale_middle():
    result = GraphUtil.rescale(10, 20, 15)
    print(result)
    assert result == 4, "should_rescale_middle"

O = [0, 0, 0]  # Black
R = [255, 0, 0]  # Red
G = [0, 255, 0]  # Green

def should_make_matrix_from_list():
    result = GraphUtil.list_to_matrix([
        O, O, O, O, O, O, O, R,
        O, O, O, O, O, O, O, R,
        O, O, O, O, O, O, O, R,
        O, O, O, O, O, O, O, R,
        O, O, O, O, O, O, O, R,
        O, O, O, O, O, O, O, R,
        O, O, O, O, O, O, O, R,
        O, O, O, O, O, O, O, R
        ])
    PrettyPrint.prettyPrint(result)
    assert result == [
        [O, O, O, O, O, O, O, O],
        [O, O, O, O, O, O, O, O],
        [O, O, O, O, O, O, O, O],
        [O, O, O, O, O, O, O, O],
        [O, O, O, O, O, O, O, O],
        [O, O, O, O, O, O, O, O],
        [O, O, O, O, O, O, O, O],
        [R, R, R, R, R, R, R, R]
        ], "should_make_matrix_from_list"

def should_left_shift_matrix_by_one():
    matrix = [
        [O, O, O, O, O, O, O, R],
        [O, O, O, O, O, O, O, R],
        [O, O, O, O, O, O, O, R],
        [O, O, O, O, O, O, O, R],
        [O, O, O, O, O, O, O, R],
        [O, O, O, O, O, O, O, R],
        [O, O, O, O, O, O, O, R],
        [O, O, O, O, O, O, O, R]
        ]
    result = GraphUtil.shiftLeftMatrix(matrix)
    PrettyPrint.prettyPrint(result)
    assert result == [
        [O, O, O, O, O, O, R, O],
        [O, O, O, O, O, O, R, O],
        [O, O, O, O, O, O, R, O],
        [O, O, O, O, O, O, R, O],
        [O, O, O, O, O, O, R, O],
        [O, O, O, O, O, O, R, O],
        [O, O, O, O, O, O, R, O],
        [O, O, O, O, O, O, R, O]
        ], "should_left_shift_matrix_by_one"


if __name__ == "__main__":
    should_rescale_less_than_min()
    should_rescale_more_than_max()
    should_rescale_min()
    should_rescale_max()
    should_rescale_middle()
    should_make_matrix_from_list()
    should_left_shift_matrix_by_one()
    print("Tests passed")



