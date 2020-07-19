#GRAPH IMPLEMENTATION [DIRECTED GRAPH] USING ADJACENCY LIST

def add_vertex(v):
    global graph
    global vertices_no
    if v in graph:
        print("Vertex ", v , " alreadu exists.")
    else:
        vertices_no += 1
        graph[v] = []



def add_edge(v1,v2,e):
    global graph
    #global vertices_no
    if v1 not in graph:
        print("Vertex ", v1 , " not in Graph")
    elif v2 not in graph:
        print("Vertex ", v2 , " not in Graph")
    else:
        temp = [v2,e]
        graph[v1].append(temp)

def print_graph():
    global graph
    for vertex in graph:
        for edges in graph[vertex]:
            print(vertex, " -> ", edges[0], " edges weight: ", edges[1])

if __name__ == "__main__":
    graph = {}
    vertices_no = 0
    
    #ADDING VERTICES
    add_vertex(1)
    add_vertex(2)
    add_vertex(3)
    add_vertex(4)

    #ADDING EDGES
    add_edge(1, 2, 1)
    add_edge(1, 3, 1)
    add_edge(2, 3, 3)
    add_edge(3, 4, 4)
    add_edge(4, 1, 5)

    #PRINT GRAPH
    print_graph()

    #PRINTING INTERNAL GRAPH
    print("Internal representation: ", graph)
    
    
    
