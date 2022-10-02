from Graph import Graph
from PrettyPrint import pretty_print_list

R = [255, 0, 0]  # Red
G = [0, 255, 0]  # Green
B = [0, 0, 255]  # Blue
O = [0, 0, 0]


def should_render_min_value():
    name_of_test = "should_render_min_value"
    graph = Graph(20, 40)
    result = graph.render(20)
    pretty_print_list(name_of_test, result)
    assert result == [
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, B
            ], name_of_test


def should_render_scaled_to_middle():
    name_of_test = "should_render_scaled_to_middle"
    graph = Graph(20, 30)
    result = graph.render(25)
    pretty_print_list(name_of_test, result)
    assert result == [
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, G,
            O, O, O, O, O, O, O, G,
            O, O, O, O, O, O, O, B,
            O, O, O, O, O, O, O, B
            ], name_of_test


def should_render_multiple_times_and_shifting_old_values_left():
    name_of_test = "should_render_multiple_times_and_shifting_old_values_left"
    graph = Graph(20, 30)
    graph.render(30)
    graph.render(25)
    result = graph.render(20)
    pretty_print_list(name_of_test, result)
    assert result == [
            O, O, O, O, O, R, O, O,
            O, O, O, O, O, R, O, O,
            O, O, O, O, O, G, O, O,
            O, O, O, O, O, G, O, O,
            O, O, O, O, O, G, G, O,
            O, O, O, O, O, G, G, O,
            O, O, O, O, O, B, B, O,
            O, O, O, O, O, B, B, B
            ], name_of_test


if __name__ == "__main__":
    should_render_min_value()
    should_render_scaled_to_middle()
    should_render_multiple_times_and_shifting_old_values_left()
    print("Tests passed")

