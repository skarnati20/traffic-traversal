from graph import TrafficGraph

graph = TrafficGraph()

print("basic.txt Result:")
graph.read_graph_from_file("examples/basic.txt")
print(graph.a_star_multi_traversal([("a", "d"), ("a", "d")]))
print(graph.prioritized_planning_traversal([("a", "d"), ("a", "d")]))
print(graph.m_star_traversal_priority([("a", "d"), ("a", "d")]))
print(graph.m_star_traversal_complete([("a", "d"), ("a", "d")]))
print("Optimal Paths:")
print(graph.find_optimal_solutions([("a", "d"), ("a", "d")]))

print("~~~\n")

print("hexagon.txt Result:")
graph.read_graph_from_file("examples/hexagon.txt")
print(graph.a_star_multi_traversal([("a", "h"), ("a", "h")]))
print(graph.prioritized_planning_traversal([("a", "h"), ("a", "h")]))
print(graph.m_star_traversal_priority([("a", "h"), ("a", "h")]))
print(graph.m_star_traversal_complete([("a", "h"), ("a", "h")]))
print("Optimal Paths:")
print(graph.find_optimal_solutions([("a", "h"), ("a", "h")]))

print("~~~\n")

print("random_selfish_1.txt Result:")
graph.read_graph_from_file("selfish-examples/random_selfish_1.txt")
print(graph.a_star_multi_traversal([("0", "49"), ("0", "49")]))
print(graph.prioritized_planning_traversal([("0", "49"), ("0", "49")]))
print(graph.m_star_traversal_priority([("0", "49"), ("0", "49")]))
print(graph.m_star_traversal_complete([("0", "49"), ("0", "49")]))
print("Optimal Paths:")
print(graph.find_optimal_solutions([("0", "49"), ("0", "49")]))

print("\n")
print("Algorithm Results")
print(
    "Prioritized: "
    + str(
        graph.prioritized_planning_traversal([("0", "49"), ("0", "49")])
        in graph.find_optimal_solutions([("0", "49"), ("0", "49")])
    )
)
print(
    "M* Priority: "
    + str(
        graph.m_star_traversal_priority([("0", "49"), ("0", "49")])
        in graph.find_optimal_solutions([("0", "49"), ("0", "49")])
    )
)
print(
    "M* Complete: "
    + str(
        graph.m_star_traversal_complete([("0", "49"), ("0", "49")])
        in graph.find_optimal_solutions([("0", "49"), ("0", "49")])
    )
)
