"""
DFS algorithim traverses the depth of any particular path in the
graph before traversing its breadth. Child nodes are visited first before sibling
nodes

The STACK data structure is used to implement the DFS algorithm
"""

graph = dict()
graph["A"] = ['B', 'C']
graph["B"] = ['E', 'C', 'A']
graph["C"] = ['A', 'B', 'E', 'F']
graph["E"] = ['B', 'C']
graph["F"] = ['C']


# It begins by creating a list to store a visited nodes.
# The graph-stack stack var is used to aid the traversal process.
# We are using a regular python list as a stack
def depth_first_search(graph, root):
    visited_vertices = list()
    graph_stack = list()

    graph_stack.append(root)
    node = root

    # body of the while loop will be executed proving the stack is not empty

    while len(graph_stack) > 0:
        if node not in visited_vertices:
            visited_vertices.append(node)
        adj_nodes = graph[node]
        if set(adj_nodes).issubset(set(visited_vertices)):
            graph_stack.pop()
            if len(graph_stack) > 0:
                node = graph_stack[-1]
            continue
        else:
            remaining_elements = set(adj_nodes).difference(set(visited_vertices))
        first_adj_node = sorted(remaining_elements)[0]
        graph_stack.append(first_adj_node)
        node = first_adj_node
    return visited_vertices


print(depth_first_search(graph, 'A'))
