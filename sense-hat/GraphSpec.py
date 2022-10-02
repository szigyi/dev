from Graph import Graph

R = [255, 0, 0]  # Red
G = [0, 255, 0]  # Green
B = [0, 0, 255]  # Blue
O = [0, 0, 0]

def should_render_min_value():
    graph = Graph(20, 40)
    result = graph.render(20)
    print(result)
    assert result == [
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            B, B, B, B, B, B, B, B
            ], "should_render_min_value"

def should_render_scaled_to_middle():
    graph = Graph(1, 8)
    result = graph.render(4)
    print(result)
    assert result == [
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            O, O, O, O, O, O, O, O,
            G, G, G, G, G, G, G, G,
            G, G, G, G, G, G, G, G,
            B, B, B, B, B, B, B, B,
            B, B, B, B, B, B, B, B
            ], "should_render_scaled_to_middle"


if __name__ == "__main__":
    should_render_min_value()
    should_render_scaled_to_middle()
    print("Tests passed")
    
    
    
    