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
    pass  # implement task 2 here by removing that pass


def dijkstras_path_finder(G: Graph, src: tuple[int, int], trg: tuple[int, int]
                          ) -> list[tuple[int, int]]:
    pass  # implement task 3 here by removing that pass
