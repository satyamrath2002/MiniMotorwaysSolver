from graph import Graph


def simple_graph_maker(dim: tuple[int, int],
                       roads: list[tuple[tuple[int, int], tuple[int, int]]]
                       ) -> Graph:
    # initializing the graph
    g = Graph(rows=dim[0], cols=dim[1])

    # creating a set of all the nodes connected by at least 1 road
    nodes = set()
    for road in roads:
        nodes.add(road[0])
        nodes.add(road[1])

    # adding all the nodes to the graph
    for node in nodes:
        g.addNode(node)

    # adding edges between each pair of nodes connected by a road
    for node1, node2 in roads:
        g.addEdge(node1, node2, [node2])
        g.addEdge(node2, node1, [node1])
    return g


def bfs_path_finder(G: Graph, src: tuple[int, int], trg: tuple[int, int]
                    ) -> list[tuple[int, int]]:
    pass  # implement task 1 here by removing that pass


def dfs_graph_maker(dim: tuple[int, int],
                    roads: list[tuple[tuple[int, int], tuple[int, int]]]
                    ) -> Graph:
    cols = dim[1]
    g_simple =  simple_graph_maker(dim,roads)
    g_dfs = Graph(rows=dim[0], cols=dim[1])
    #implement dfs in g_simple and analyse each node
    nodes = g_simple.getNodes() 
    for node in nodes:
        if len(g_simple._getAdjDict(node)) != 2:
            start = node
            break

    pos_start = start[0] + cols*start[1]
    stack = queue.LifoQueue(maxsize = -1)
    visited = []
    path = []  #path is the list of nodes traversed      
    stack.put((pos_start, path))
    visited.append(pos_start)
    ######Check if the starting node has 2 nodes or not. If it has 2 nodes, then in g_dfs, 
    # add the two neighbors as an edge along with the path else simply add the nodes and corresponding edges
    while not stack.empty():
        
        vertex, path = stack.get()

        if len(g_simple._getAdjDict((vertex%cols, vertex//cols))) == 2:
            path.append((vertex%cols, vertex//cols))

        elif len(g_simple._getAdjDict((vertex%cols, vertex//cols))) != 2:
            g_dfs.addNode((vertex%cols, vertex//cols))

            if len(path) != 0:
                g_dfs.addEdge((vertex%cols, vertex//cols),path[0],path)
                path_reverse = path[::-1]
                g_dfs.addEdge(path[0],(vertex%cols, vertex//cols), path_reverse)
            
            path = [(vertex%cols, vertex//cols)]


        for neighbor in g_simple._getAdjDict((vertex%cols,vertex//cols)):#neighbor is position of nodes adjacent to "vertex"
            if neighbor not in visited:
                visited.append(neighbor)
                stack.put((neighbor, path))

    return g_dfs



def dijkstras_path_finder(G: Graph, src: tuple[int, int], trg: tuple[int, int]
                          ) -> list[tuple[int, int]]:
    pass  # implement task 3 here by removing that pass
