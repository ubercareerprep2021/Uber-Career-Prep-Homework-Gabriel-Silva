class TreeNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def print_node(self):
        if self is None:
            return
        else:
            print(self.data)
            if self.left is not None:
                self.left.print_node()
            if self.right is not None:
                self.right.print_node()

class TreeEmployee:
    def __init__(self, name: str, title: str, direct_reports: list):
        self.name = name
        self.title = title
        self.direct_reports = direct_reports

    def print_level_by_level(self):
        if self is None:
            return
        else:
            level_list = [self]
            while len(level_list) > 0:
                next_level_list = list()
                for element in level_list:
                    print("Name: {}, Title: {}".format(element.name, element.title))
                    if len(element.direct_reports) > 0:
                        for direct_report in element.direct_reports:
                            next_level_list.append(direct_report)
                level_list = next_level_list

    def print_num_levels(self):
        if self is None:
            return
        else:
            level_counter = 0
            level_list = [self]
            while len(level_list) > 0:
                next_level_list = list()
                for element in level_list:
                    if len(element.direct_reports) > 0:
                        for direct_report in element.direct_reports:
                            next_level_list.append(direct_report)
                level_counter += 1
                level_list = next_level_list
            print(level_counter)


if __name__ == "__main__":
    I = TreeEmployee("I", "Director", [])
    B = TreeEmployee("B", "CFO", [I])
    F = TreeEmployee("F", "Engineer", [])
    G = TreeEmployee("G", "Engineer", [])
    H = TreeEmployee("H", "Engineer", [])
    D = TreeEmployee("D", "Manager", [F, G, H])
    E = TreeEmployee("E", "Manager", [])
    C = TreeEmployee("C", "CTO", [D, E])
    A = TreeEmployee("A", "CEO", [B, C])

    A.print_num_levels()