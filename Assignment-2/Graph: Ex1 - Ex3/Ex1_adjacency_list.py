class GraphNode:
    def __init__(self, data):
        self.data = data


class GraphWithAdjacencyList:
    def __init__(self):
        self.map = {}

    def add_node(self, key: GraphNode):
        self.map[key] = []

    def remove_node(self, key: GraphNode):
        self.map.pop(key, None)

    def add_edge(self, node_1: GraphNode, node_2: GraphNode):
        """ since it's an undirected graph, both nodes were added to
            each others list """
        self.map[node_1].append(node_2)
        self.map[node_2].append(node_1)

    def remove_edge(self, node_1: GraphNode, node_2: GraphNode):
        """ since it's an undirected graph, both nodes were added to
            each others list """
        self.map[node_1].remove(node_2)
        self.map[node_2].remove(node_1)


if __name__ == "__main__":
    graph = GraphWithAdjacencyList()
    node_7 = GraphNode(7)
    node_2 = GraphNode(2)
    node_4 = GraphNode(4)
    node_6 = GraphNode(6)
    node_0 = GraphNode(0)

    graph.add_node(node_7)
    graph.add_node(node_2)
    graph.add_node(node_4)

    graph.add_node(node_6)
    graph.add_node(node_0)
    graph.add_edge(node_7, node_2)
    graph.add_edge(node_7, node_4)
    # graph.add_edge(node_2, node_4)
    # graph.add_edge(node_2, node_0)
    # graph.add_edge(node_6, node_4)
    # graph.add_edge(node_6, node_0)
    print("graph 7", graph.map[node_7])
    print("graph 2", graph.map[node_2])
    graph.remove_edge(node_7, node_2)
    print("graph 7", graph.map[node_7])
    print("graph 2", graph.map[node_2])
    print("graph 4", graph.map[node_4])
    graph.remove_edge(node_7, node_4)
    print("graph 7", graph.map[node_7])
    print("graph 4", graph.map[node_4])