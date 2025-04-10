# Implementation of Binary Search Tree of Traversal
# - Inorder
# - Preorder
# - Postorder
class Node:
    def __init__(self, data):
        self.left: Node | None = None
        self.right: Node | None = None
        self.data = data


def printInOrder(root: Node | None):
    """Inorder Traversal
    Time complexity: O(N), N is the number of nodes
    Space complexity: O(h), h is the height of the tree

    Steps:
        1. Goes down the left tree
        2. Gets the value of the root
        3. Goes down the right tree
    """
    if root:
        printInOrder(root.left)
        print(root.data, end=" ")
        printInOrder(root.right)


def printPreOrder(root: Node | None):
    """Preorder Traversal
    Time complexity: O(N), N is the number of nodes
    Space complexity: O(h), h is the height of the tree

    Steps:
        1. Gets the value of the root
        2. Goes down the left tree
        3. Goes down the right tree
    """
    if root:
        print(root.data, end=" ")
        printPreOrder(root.left)
        printPreOrder(root.right)


def printPostOrder(root: Node | None):
    """Postorder Traversal
    Time complexity: O(N), N is the number of nodes
    Space complexity: O(h), h is the height of thre tree

    Steps:
        1. Goes down the left tree
        2. Goes down the right tree
        3. Gets the value of the root
    """
    if root:
        printPostOrder(root.left)
        printPostOrder(root.right)
        print(root.data, end=" ")


if __name__ == "__main__":
    # Build the tree
    root = Node(10)
    root.left = Node(4)
    root.right = Node(16)
    root.left.left = Node(1)
    root.left.right = Node(2)
    root.right.left = Node(8)
    root.right.right = Node(12)

    # Traversals
    print("Inorder Traversal:", end=" ")
    printInOrder(root)
    print()
    print("Preorder Traversal:", end=" ")
    printPreOrder(root)
    print()
    print("Postorder Traversal:", end=" ")
    printPostOrder(root)
