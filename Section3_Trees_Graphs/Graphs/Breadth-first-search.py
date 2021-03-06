"""
A queue data structure is used to store the information of vertices that are
to be visited in the graph
"""
graph = dict()
graph["A"] = ['B', 'C']
graph["B"] = ['E', 'C', 'A']
graph["C"] = ['A', 'B', 'E', 'F']
graph["E"] = ['B', 'C']
graph["F"] = ['C']
graph["Z"] = ["P"]

from collections import deque


def breadth_first_search(graph, root):
    visited_vertices = list()
    graph_queue = deque([root])
    visited_vertices.append(root)
    node = root

    while len(graph_queue) > 0:
        node = graph_queue.popleft()
        adj_nodes = graph[node]
        remaining_elements = set(adj_nodes).difference(set(visited_vertices))
        if len(remaining_elements) > 0:
            for elem in sorted(remaining_elements):
                visited_vertices.append(elem)
                graph_queue.append(elem)

    return visited_vertices


# Time complexity of BFS is O( |V| + |E|)
def hasRoute(node1, node2):
    root = node1
    visited_vertices = list()
    graph_queue = deque([root])
    visited_vertices.append(root)
    node = root
    while len(graph_queue) > 0:
        node = graph_queue.popleft()
        adj_nodes = graph[node]
        if node == node1:
            for each_node in adj_nodes:
                current_neighbor = each_node
                if current_neighbor == node2:
                    return True
        else:
            remaining_elements = set(adj_nodes).difference(set(visited_vertices))
            if len(remaining_elements) > 0:
                for elem in sorted(remaining_elements):
                    visited_vertices.append(elem)
                    graph_queue.append(elem)
    return False


print(hasRoute('Z', 'P'))