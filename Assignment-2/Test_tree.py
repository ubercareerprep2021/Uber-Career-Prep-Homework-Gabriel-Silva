import Tree as t, unittest

class TestPart1(unittest.TestCase):

    def test_tree_print_ex1(self):
        left_child = t.TreeNode(6, None, None)
        right_child = t.TreeNode(3, None, None)
        left = t.TreeNode(7, None, None)
        right = t.TreeNode(17, left_child, right_child)
        root = t.TreeNode(1, left, right)
        root.print_node()

    def test_tree_employee_print_by_level_ex2(self):
        K = t.TreeEmployee("K", "Sales Intern", [])
        J = t.TreeEmployee("J", "Sales Representative", [K])
        I = t.TreeEmployee("I", "Director", [J])
        B = t.TreeEmployee("B", "CFO", [I])
        F = t.TreeEmployee("F", "Engineer", [])
        G = t.TreeEmployee("G", "Engineer", [])
        H = t.TreeEmployee("H", "Engineer", [])
        D = t.TreeEmployee("D", "Manager", [F, G, H])
        E = t.TreeEmployee("E", "Manager", [])
        C = t.TreeEmployee("C", "CTO", [D, E])
        A = t.TreeEmployee("A", "CEO", [B, C])

        A.print_level_by_level()
        
    def test_tree_employee_level_ex3_1(self):
        K = t.TreeEmployee("K", "Sales Intern", [])
        J = t.TreeEmployee("J", "Sales Representative", [K])
        I = t.TreeEmployee("I", "Director", [J])
        B = t.TreeEmployee("B", "CFO", [I])
        F = t.TreeEmployee("F", "Engineer", [])
        G = t.TreeEmployee("G", "Engineer", [])
        H = t.TreeEmployee("H", "Engineer", [])
        D = t.TreeEmployee("D", "Manager", [F, G, H])
        E = t.TreeEmployee("E", "Manager", [])
        C = t.TreeEmployee("C", "CTO", [D, E])
        A = t.TreeEmployee("A", "CEO", [B, C])

        A.print_num_levels()
        
    def test_tree_employee_level_ex3_2(self):
        I = t.TreeEmployee("I", "Director", [])
        B = t.TreeEmployee("B", "CFO", [I])
        F = t.TreeEmployee("F", "Engineer", [])
        G = t.TreeEmployee("G", "Engineer", [])
        H = t.TreeEmployee("H", "Engineer", [])
        D = t.TreeEmployee("D", "Manager", [F, G, H])
        E = t.TreeEmployee("E", "Manager", [])
        C = t.TreeEmployee("C", "CTO", [D, E])
        A = t.TreeEmployee("A", "CEO", [B, C])

        A.print_num_levels()

if __name__ == '__main__':
    unittest.main()