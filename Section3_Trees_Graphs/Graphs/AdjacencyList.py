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
"""