from typing import Optional, Tuple

class Node:
    def __init__(self, data: Optional[int] = None):
        """Inicializace uzlu s daty, levým a pravým podstromem."""
        self.data: Optional[int] = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def insert(self, data: int) -> None:
        """Vložení nové hodnoty do stromu."""
        if self.data is not None:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def contains(self, data: int) -> Tuple[bool, int]:
        """Zjištění, zda strom obsahuje zadanou hodnotu.
        Vrací dvojici: (nalezeno, počet kroků)."""
        steps = 0
        current = self

        while current:
            steps += 1
            if current.data == data:
                return True, steps
            elif data < current.data:
                current = current.left
            else:
                current = current.right

        return False, steps

    def breadth_first_search(self, data: int) -> Tuple[bool, int]:
        """Vyhledávání zadané hodnoty pomocí BFS (Breadth-First Search).
        Vrací dvojici: (nalezeno, počet kroků)."""
        if not self:
            return False, 0

        queue = [self]
        steps = 0

        while queue:
            current = queue.pop(0)
            steps += 1

            if current.data == data:
                return True, steps

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return False, steps

    def print_tree(self, level: int = 0, prefix: str = "") -> None:
        """Výpis stromu jako text s odsazením."""
        if self.data is not None:
            print(" " * (4 * level) + prefix + str(self.data))
            if self.left:
                self.left.print_tree(level + 1, "L: ")
            if self.right:
                self.right.print_tree(level + 1, "R: ")

    def pretty_print(self, level: int = 0, space: int = 4) -> None:
        """Symetrický výpis stromu zachovávající jeho strukturu."""

        def print_level(nodes: list[Optional[Node]], level: int, max_depth: int) -> None:
            if not any(nodes):
                return

            indent = " " * (2 ** (max_depth - level) * space)
            row = ""
            next_nodes = []

            for node in nodes:
                if node:
                    row += f"{indent}{node.data}{indent}"
                    next_nodes.extend([node.left, node.right])
                else:
                    row += f"{indent}{' '}{indent}"
                    next_nodes.extend([None, None])

            print(row)
            print_level(next_nodes, level + 1, max_depth)

        max_depth = self.max_depth()
        print_level([self], 1, max_depth)

    def max_depth(self) -> int:
        """Výpočet maximální hloubky stromu."""
        left_depth = self.left.max_depth() if self.left else 0
        right_depth = self.right.max_depth() if self.right else 0
        return 1 + max(left_depth, right_depth)


# Testování funkcionality stromu
if __name__ == "__main__":
    bin_tree = Node(10)
    bin_tree.insert(6)
    bin_tree.insert(14)
    bin_tree.insert(5)
    bin_tree.insert(8)
    bin_tree.insert(11)
    bin_tree.insert(18)
    bin_tree.insert(1)
    bin_tree.insert(20)
    bin_tree.insert(25)

    # Testování metody breadth_first_search
    assert bin_tree.breadth_first_search(10) == (True, 1)
    assert bin_tree.contains(10) == (True, 1)
    assert bin_tree.breadth_first_search(18) == (True, 7)
    assert bin_tree.contains(18) == (True, 3)
    assert bin_tree.breadth_first_search(11) == (True, 6)
    assert bin_tree.contains(11) == (True, 3)
    assert bin_tree.breadth_first_search(55) == (False, 10)

    print("All tests passed!")
    print("\nVizualizace stromu:")
    bin_tree.pretty_print()
