# added visited node parameter to check if node has been visited and stop infinite loops
class GraphNode:
    def __init__(self, data):
        self.data = data
        #self.visited_node = False


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
        """ since it's an undirected graph, both nodes were removed from
            each others list """
        self.map[node_1].remove(node_2)
        self.map[node_2].remove(node_1)

    def get_adj_nodes(self, node: GraphNode):
        return self.map[node]

    def depth_first_search(self, node: GraphNode, check_dict: dict):
        print(node.data)
        #insert node on dictionary to check if node has been visited
        check_dict[node] = True
        for close_item in self.map[node]:
            #if node hasn't been visited, go into recursion
            if check_dict.get(close_item) is None:
                self.depth_first_search(close_item, check_dict)
        return
        

if __name__ == "__main__":
    graph = GraphWithAdjacencyList()
    node_7 = GraphNode(7)
    node_2 = GraphNode(2)
    node_4 = GraphNode(4)
    node_6 = GraphNode(6)
    node_0 = GraphNode(0)
    node_10 = GraphNode(10)
    node_20 = GraphNode(20)
    node_30 = GraphNode(30)

    graph.add_node(node_7)
    graph.add_node(node_2)
    graph.add_node(node_4)
    graph.add_node(node_6)
    graph.add_node(node_0)
    graph.add_node(node_10)
    graph.add_node(node_20)
    graph.add_node(node_30)

    graph.add_edge(node_7, node_2)
    graph.add_edge(node_7, node_4)
    graph.add_edge(node_0, node_10)
    graph.add_edge(node_2, node_0)
    graph.add_edge(node_6, node_4)
    graph.add_edge(node_6, node_0)
    graph.add_edge(node_10, node_20)
    graph.add_edge(node_20, node_30)
    
    # graph.add_edge() order matters on DFS
    # result 7 2 0 10 20 30 6 4
    graph.depth_first_search(node_7, {})

