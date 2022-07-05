import random
from random import randrange
from Graph import Graph
from Vertex import Vertex


def print_graph(graph):
    for vertex in graph.graph_dict:
        print("")
        print(vertex + " connected to")
        vertex_neighbors = graph.graph_dict[vertex].edges
        if len(vertex_neighbors) == 0:
            print("No edges!")
        for adjacent_vertex in vertex_neighbors:
            print("=> " + adjacent_vertex)


def build_tsp_graph(directed):
    g = Graph(directed)
    vertices = []
    for val in ['a', 'b', 'c', 'd']:
        vertex = Vertex(val)
        vertices.append(vertex)
        g.add_vertex(vertex)

    g.add_edge(vertices[0], vertices[1], 3)
    g.add_edge(vertices[0], vertices[2], 4)
    g.add_edge(vertices[0], vertices[3], 5)
    g.add_edge(vertices[1], vertices[0], 3)
    g.add_edge(vertices[1], vertices[2], 2)
    g.add_edge(vertices[1], vertices[3], 6)
    g.add_edge(vertices[2], vertices[0], 4)
    g.add_edge(vertices[2], vertices[1], 2)
    g.add_edge(vertices[2], vertices[3], 1)
    g.add_edge(vertices[3], vertices[0], 5)
    g.add_edge(vertices[3], vertices[1], 6)
    g.add_edge(vertices[3], vertices[2], 1)
    return g


def visited_all_nodes(visitedVertices):
    # visitedVeritices is a dictionary of form {<vertex>:'<unvisited | visited>'}
    for vertex in visitedVertices:
        if visitedVertices[vertex] == "unvisited":
            return False

    return True


def traveling_salesperson(graph):
    finalPath = ""
    visitedVertices = {x: "unvisited" for x in graph.graph_dict}
    current_vertex = random.choice(list(graph.graph_dict))
    visitedVertices[current_vertex] = "visited"
    finalPath += current_vertex
    # To check if we’ve visited all the vertices in visitedVertices
    visitedAllVertices = visited_all_nodes(visitedVertices)
    while not visitedAllVertices:
        current_vertex_edges = graph.graph_dict[current_vertex].get_edges()
        current_vertex_edge_weights = {}
        for edge in current_vertex_edges:
            current_vertex_edge_weights[edge] = graph.graph_dict[current_vertex].get_edge_weight(
                edge)
        found_next_vertex = False
        next_vertex = ""
        while not found_next_vertex:
            if current_vertex_edge_weights is None:
                break
            next_vertex = min(current_vertex_edge_weights,
                                    key=current_vertex_edge_weights.get)
            # Check whether it points to a vertex that has already been visited or not
            if visitedVertices[next_vertex] == "visited":
                # If visited, pop the edge from our dictionary and continue searching
                current_vertex_edge_weights.pop(next_vertex)
            else:
                # If unvisited, found our next_vertex
                found_next_vertex = True
            # If dictionary of current vertex edge weights empty, break process of finding next vertices by setting visited_all_vertices to True
            if current_vertex_edge_weights is None:
                visited_all_vertices = True
            else:
                current_vertex = next_vertex
                visitedVertices[current_vertex] = "visited"
                finalPath += current_vertex

        visitedAllVertices = visited_all_nodes(visitedVertices)

    print(finalPath)


graph = build_tsp_graph(False)
traveling_salesperson(graph)
