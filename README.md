# Traffic Traversal

An investigation into path traversal algorithms for changing-cost graphs.

## The Problem

Path traversal algorithms like Djikstra's and A* Search are popular for simple path traversals where the graph contains edges of a fixed cost. Imagine, though, that two agents tried to cross the same edge at the same time, but this time the cost of taking that edge went up by 50%! Such an example isn't far off reality, as map apps like Waze or Google Maps may be affecting traffic patterns by sending loads of cars on the same "optimal" path. How could they spread this traffic out? How could we design an algorithm to find an optimal path for each agent that considers this sort of rule?

A similar domain of path traversal algorithms exist for the Multi-Agent Path Finding problem (MAPF), in which two actors may not occupy the same space at a given time step. However most optimal but efficient algorithms for this problem space don't exactly translate to the above problem.

Let's define some constraints:
* Edge weights are positive
* For each additional agent travelling an edge already occupied by one agent, the edge increases its weight by 50% of the base weight
* We will not consider graphs with cycles

## Approaches

Here are the approaches implemented in this repository. A brief explanation of each is provided:

### 1. A* Traversal

A simple but certainly not optimal solution involving generating the A* path for each agent. While a quick solution, it does not consider how an edge's cost may change after two agents collide on a path.

Time Complexity at Conflict: **O(1)** (no conflicts considered)

### 2. Prioritized Planning Traversal

One approach you can take is by creating a priority queue of the agents so that the first priority agent can make the first move, the second priority agent makes the second move, etc.; if we have the nth priority agent, they will make a move based on the past n - 1 agents, perhaps avoiding a commonly taken path because it may be more costly than it initially was. This solution, though, is not optimal since we are randomly picking the order and that may prejudice against certain possibilites that might have led to the optimal solution. To minimize this possibility, the implementation here decides to re-generate the shuffled priority queue at each time step, so as to spread preference evenly among all the agents.

Time Complexity at Conflict: **O(n)** (n = number of agents)

### 3. M* (Priority) Traversal

To achieve a more optimal solution than the prioritized planning approach we can adopt strategies from an [M* Search](https://people.ucsc.edu/~dmilutin/IROS/Book/Wagner_Choset.pdf).

An M*-based approach involves allowing each agent to compute a move based on A* first. If none of the moves conflict, then we should go ahead with each move and go to the next time step. If, however, there is a conflict, we then place the current state in an "incomplete" state, meaning that it will progress incrementally. For a traversal with n agents, we would create n new traversal states where each state has one of the agents advanced by its optimal A* move. We then place them in a state of queues and when we consider each again, we will repeat the steps for the remaining unallocated actors until they have all been allocated there additional move, meaning everyone is on the same time step. In effect, this is searching every permutation of priority queues.

Time Complexity at Conflict: **O(n!)** (n = number of agents)

### 4. M* (Complete) Traversal

This is similar to the previous M* approach, except this time, in the event of conflict, we expand each agent by every possible move it could take at that time, not just its A* optimal move anymore.

Time Complexity at Conflict: **O(m^n)** (n = number of agents, m = max number of neighbors at a node)

## Random Graph Generation

In addition, there is also a function to generate random graph files based on a modified version of the [Erdos-Renyi model](https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93R%C3%A9nyi_model). It can be found in `generate_random_graph.py`.

## Usage

```{python}
from graph import TrafficGraph
from generate_random_graph import generate_random_graph

graph = TrafficGraph()

graph.add_node('first_node', 0, 1)
graph.add_node('second_node', 2, 3)
graph.add_node('third_node', -1, 5)

graph.add_edge('first_node', 'second_node', 3)
graph.add_edge('second_node', 'third_node', 8)

print(graph.a_star_single_traversal('first_node', 'third_node'))

graph.read_graph_from_file('examples/basic.txt')

print(graph.a_star_multi_traversal([('a', 'd'), ('a', 'd')]))
print(graph.prioritized_planning_traversal([('a', 'd'), ('a', 'd')]))
print(graph.m_star_traversal_priority([('a', 'd'), ('a', 'd')]))
print(graph.m_star_traversal_complete([('a', 'd'), ('a', 'd')]))

print('Optimal Paths:')
print(graph.find_optimal_solutions([('a', 'd'), ('a', 'd')]))

generate_random_graph(50, 0.10, 5, 'random.txt')
```

See `example.py` for a sample file!

## Future Work

For myself but also anyone else that's interested!

* Test out new graphs
* Optimize M* approaches - It is possible to only expand the agents which conflict with each other, and leave the rest as normal.
* Optimize approaches further
* Create new approaches
