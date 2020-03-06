"""
Graphs can be represented with two main forms while 
implementing them in Python.
One way is to use adjacency list
Another way is to use an adjacency matrix

 Here we will look at how an Adjacency list is formed

An adjacency list stores all the nodes, along with other nodes that are
directly connected them in the graph.

Two nodes A and B in  a graph G are said to be adjacent IF
there is a direct connection between them.

A LIST data structure in Python is used to represent a graph
The indices of the list can be used to represent the nodes or vertices in the graph

However, a list will not allow us to use vertex labels. Therefore, a DICTIONARY data
structure is more suitable to represent the graph.
"""
graph = dict()
graph["A"] = ['B', 'C']
graph["B"] = ['E', 'C', 'A']
graph["C"] = ['A', 'B', 'E', 'F']
graph["E"] = ['B', 'C']
graph["F"] = ['C']

"""
An Adjacency matrix can be implemented using the given adjacency list

First, we have to obtain the key elements of the adjacency matrix. 
The code to implement an adjacency matrix goes as follows
"""
matrix_elements = sorted(graph.keys())
cols = rows = len(matrix_elements) # cols and rows must be equal
adjacency_matrix = [[0 for x in range(rows)] for y in range(cols)] # Empty matrix size NxM
edges_list = []
# The multi-d array is filled using a nested for loop
for key in matrix_elements:
    for neighbor in graph[key]:
        edges_list.append((key, neighbor))
print(edges_list)
"""
Next step is to fill it using 1 to denote the presense of an edge in the grpah. 
"""
for edge in edges_list:
    index_of_first_vertex = matrix_elements.index(edge[0])
    index_of_second_vertex = matrix_elements.index(edge[1])
    adjacency_matrix[index_of_first_vertex][index_of_second_vertex] = 1

