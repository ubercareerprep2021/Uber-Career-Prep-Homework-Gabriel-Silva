import Part1_tree, unittest

class TestPart1(unittest.TestCase):

    def test_tree_print_ex1(self):
        left_child = Part1.TreeNode(6, None, None)
        right_child = Part1.TreeNode(3, None, None)
        left = Part1.TreeNode(7, None, None)
        right = Part1.TreeNode(17, left_child, right_child)
        root = Part1.TreeNode(1, left, right)
        root.print_node()

    def test_tree_employee_print_by_level_ex2(self):
        K = Part1.TreeEmployee("K", "Sales Intern", [])
        J = Part1.TreeEmployee("J", "Sales Representative", [K])
        I = Part1.TreeEmployee("I", "Director", [J])
        B = Part1.TreeEmployee("B", "CFO", [I])
        F = Part1.TreeEmployee("F", "Engineer", [])
        G = Part1.TreeEmployee("G", "Engineer", [])
        H = Part1.TreeEmployee("H", "Engineer", [])
        D = Part1.TreeEmployee("D", "Manager", [F, G, H])
        E = Part1.TreeEmployee("E", "Manager", [])
        C = Part1.TreeEmployee("C", "CTO", [D, E])
        A = Part1.TreeEmployee("A", "CEO", [B, C])

        A.print_level_by_level()
        
    def test_tree_employee_level_ex3_1(self):
        K = Part1.TreeEmployee("K", "Sales Intern", [])
        J = Part1.TreeEmployee("J", "Sales Representative", [K])
        I = Part1.TreeEmployee("I", "Director", [J])
        B = Part1.TreeEmployee("B", "CFO", [I])
        F = Part1.TreeEmployee("F", "Engineer", [])
        G = Part1.TreeEmployee("G", "Engineer", [])
        H = Part1.TreeEmployee("H", "Engineer", [])
        D = Part1.TreeEmployee("D", "Manager", [F, G, H])
        E = Part1.TreeEmployee("E", "Manager", [])
        C = Part1.TreeEmployee("C", "CTO", [D, E])
        A = Part1.TreeEmployee("A", "CEO", [B, C])

        A.print_num_levels()
        
    def test_tree_employee_level_ex3_2(self):
        I = Part1.TreeEmployee("I", "Director", [])
        B = Part1.TreeEmployee("B", "CFO", [I])
        F = Part1.TreeEmployee("F", "Engineer", [])
        G = Part1.TreeEmployee("G", "Engineer", [])
        H = Part1.TreeEmployee("H", "Engineer", [])
        D = Part1.TreeEmployee("D", "Manager", [F, G, H])
        E = Part1.TreeEmployee("E", "Manager", [])
        C = Part1.TreeEmployee("C", "CTO", [D, E])
        A = Part1.TreeEmployee("A", "CEO", [B, C])

        A.print_num_levels()

if __name__ == '__main__':
    unittest.main()