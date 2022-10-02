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


o = [0, 0, 0]  # Black
R = [255, 0, 0]  # Red
G = [0, 255, 0]  # Green


def should_make_matrix_from_list():
    name_of_test = "should_make_matrix_from_list"
    result = GraphUtil.list_to_matrix([
        o, o, o, o, o, o, o, R,
        o, o, o, o, o, o, o, R,
        o, o, o, o, o, o, o, R,
        o, o, o, o, o, o, o, R,
        o, o, o, o, o, o, o, R,
        o, o, o, o, o, o, o, R,
        o, o, o, o, o, o, o, R,
        o, o, o, o, o, o, o, R
        ])
    PrettyPrint.pretty_print(name_of_test, result)
    assert result == [
        [o, o, o, o, o, o, o, R],
        [o, o, o, o, o, o, o, R],
        [o, o, o, o, o, o, o, R],
        [o, o, o, o, o, o, o, R],
        [o, o, o, o, o, o, o, R],
        [o, o, o, o, o, o, o, R],
        [o, o, o, o, o, o, o, R],
        [o, o, o, o, o, o, o, R]
        ], name_of_test


def should_left_shift_matrix_by_one():
    name_of_test = "should_left_shift_matrix_by_one"
    matrix = [
        [o, o, o, o, o, o, o, R],
        [o, o, o, o, o, o, o, R],
        [o, o, o, o, o, o, o, R],
        [o, o, o, o, o, o, o, R],
        [o, o, o, o, o, o, o, R],
        [o, o, o, o, o, o, o, R],
        [o, o, o, o, o, o, o, R],
        [o, o, o, o, o, o, o, R]
        ]
    result = GraphUtil.shift_left_matrix(matrix)
    PrettyPrint.pretty_print(name_of_test, result)
    assert result == [
        [o, o, o, o, o, o, R, o],
        [o, o, o, o, o, o, R, o],
        [o, o, o, o, o, o, R, o],
        [o, o, o, o, o, o, R, o],
        [o, o, o, o, o, o, R, o],
        [o, o, o, o, o, o, R, o],
        [o, o, o, o, o, o, R, o],
        [o, o, o, o, o, o, R, o]
        ], name_of_test


if __name__ == "__main__":
    should_rescale_less_than_min()
    should_rescale_more_than_max()
    should_rescale_min()
    should_rescale_max()
    should_rescale_middle()
    should_make_matrix_from_list()
    should_left_shift_matrix_by_one()
    print("Tests passed")



