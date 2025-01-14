import random


def generate_random_graph(
    num_nodes: int, edge_probability: float, edge_weight_max: int, output_file: str
):
    """
    Creates a random graph file based off a tweaked version of the Erdos-Renyi
    model. It generates the number of nodes that the user specifies and proceeds
    to create edges for each node that appears afterward based on a fixed
    probability. It also randomly generates an edge weight integer when the
    user provides a max edge weight.

    Parameters
    __________
    num_nodes : int
        The number of nodes to create in the graph
    edge_probability : float
        The probability (between 0 and 1 inclusive) of an edge occuring for
        a pair of nodes
    edge_weight_max : int
        The maximum for the model's random edge weight generation
    output_file : str
        The file to write the graph to
    """
    if num_nodes < 0:
        print("Error: num nodes argument can't be negative")
        return
    if edge_probability > 1 or edge_probability < 0:
        print("Error: edge probability argument must be between 0 and 1 inclusive")
        return
    if edge_weight_max <= 0:
        print("Error: edge weight max argument must be a positive integer")

    # Generate nodes and create edges based on probability (edge creation is in
    # a forward direction only)
    nodes = []
    edges = []
    for i in range(num_nodes):
        nodes.append((i, 0, i))
        for j in range(i + 1, num_nodes):
            # Create an edge based off the probability
            if random.random() < edge_probability:
                weight = random.randint(1, edge_weight_max)
                edges.append((i, j, weight))

    # Write to file in proper format
    with open(output_file, "w") as file:
        for n, x, y in nodes:
            file.write(str(n) + "," + str(x) + "," + str(y) + "\n")
        file.write("\n")
        for a, b, w in edges:
            file.write(str(a) + "," + str(b) + "," + str(w) + "\n")
