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
        """ since it's an undirected graph, both nodes were removed from
            each others list """
        self.map[node_1].remove(node_2)
        self.map[node_2].remove(node_1)

    def get_adj_nodes(self, node: GraphNode):
        return self.map[node]

    def check_courses(self, prerequisites: list):
        pre_course = {}
        
        for pre_req in prerequisites:
            # if the course Bi is in the Ai in another prerequisite, returns false
            if pre_course.get(pre_req[0]) is True:
                return False
            else:
                # add Ai to a dictionary to keep track
                pre_course[pre_req[1]]= True
        
        return True


if __name__ == "__main__":
    graph = GraphWithAdjacencyList()
    node_0 = GraphNode(0)
    node_1 = GraphNode(1)
    node_2 = GraphNode(2)
    node_3 = GraphNode(3)
    node_4 = GraphNode(4)

    print(graph.check_courses([[node_1, node_0]]))
    print(graph.check_courses([[node_1, node_0], [node_0, node_1]]))
    print(graph.check_courses([[node_1, node_0], [node_2, node_1], [node_3, node_2], [node_4, node_3]]))
    print(graph.check_courses([[node_1, node_0], [node_2, node_1], [node_4, node_3], [node_3, node_2]]))
