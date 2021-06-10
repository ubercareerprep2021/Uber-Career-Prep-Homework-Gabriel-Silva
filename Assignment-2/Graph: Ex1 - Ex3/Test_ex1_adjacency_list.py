import Ex1_adjacency_list as t, unittest

class TestGraphEx1(unittest.TestCase):

    def test_graph_insertion_and_removal(self):
        graph = t.GraphWithAdjacencyList()
        node_1 = t.GraphNode(7)
        node_2 = t.GraphNode(2)
        graph.add_node(node_1)
        graph.add_node(node_2)
        self.assertEqual(len(graph.map), 2)
        graph.remove_node(node_2)
        self.assertEqual(len(graph.map), 1)
        graph.remove_node(node_1)
        self.assertEqual(len(graph.map), 0)

    def test_add_edges(self):
        graph  = t.GraphWithAdjacencyList()
        node_7 = t.GraphNode(7)
        node_2 = t.GraphNode(2)
        node_4 = t.GraphNode(4)
        node_6 = t.GraphNode(6)
        node_0 = t.GraphNode(0)

        graph.add_node(node_7)
        graph.add_node(node_2)
        graph.add_node(node_4)
        graph.add_node(node_6)
        graph.add_node(node_0)
        graph.add_edge(node_7, node_2)
        self.assertEqual(graph.map[node_7][0], node_2)
        graph.add_edge(node_7, node_4)
        self.assertEqual(graph.map[node_7][1], node_4)
        graph.add_edge(node_2, node_4)
        self.assertEqual(graph.map[node_2][1], node_4)
        graph.add_edge(node_2, node_0)
        self.assertEqual(graph.map[node_2][2], node_0)
        graph.add_edge(node_6, node_4)
        self.assertEqual(graph.map[node_4][2], node_6)
        graph.add_edge(node_6, node_0)
        self.assertEqual(graph.map[node_0][1], node_6)

    def test_remove_edges(self):
        graph  = t.GraphWithAdjacencyList()
        node_7 = t.GraphNode(7)
        node_2 = t.GraphNode(2)
        node_4 = t.GraphNode(4)

        graph.add_node(node_7)
        graph.add_node(node_2)
        graph.add_node(node_4)
        graph.add_edge(node_7, node_2)
        graph.add_edge(node_7, node_4)
        graph.add_edge(node_2, node_4)
        self.assertEqual(graph.map[node_7][1], node_4)
        graph.remove_edge(node_7, node_2)
        self.assertEqual(graph.map[node_7][0], node_4)
        self.assertEqual(graph.map[node_2][0], node_4)
        graph.remove_edge(node_7, node_4)
        self.assertEqual(len(graph.map[node_7]), 0)
        self.assertEqual(graph.map[node_4][0], node_2)
        graph.remove_edge(node_2, node_4)
        self.assertEqual(len(graph.map[node_2]), 0)
        self.assertEqual(len(graph.map[node_4]), 0)


    def test_get_adj_nodes(self):
        graph  = t.GraphWithAdjacencyList()
        node_7 = t.GraphNode(7)
        node_2 = t.GraphNode(2)
        node_4 = t.GraphNode(4)

        graph.add_node(node_7)
        graph.add_node(node_2)
        graph.add_node(node_4)
        graph.add_edge(node_7, node_2)
        graph.add_edge(node_7, node_4)
        graph.add_edge(node_2, node_4)
        self.assertEqual(graph.get_adj_nodes(node_2), [node_7, node_4])
        self.assertEqual(graph.get_adj_nodes(node_7), [node_2, node_4])

if __name__ == '__main__':
    unittest.main()