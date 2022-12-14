class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = Node('F',
            Node('B',
                 Node('A'),
                 Node('D',
                      Node('C'), Node('E'))),
            Node('G',
                 None,
                 Node('I', Node('H'))
                 )
            )


def preorder(node):
    stack = []
    stack.append(node)

    while stack and node:
        node = stack.pop()

        print(node.val, end=" ")

        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)


def inorder(node):
    stack = []
    current_node = node
    stack.append(current_node)

    while stack:
        while current_node:
            stack.append(current_node)
            current_node = current_node.left

        current_node = stack.pop()

        print(current_node.val, end=" ")

        current_node = current_node.right


def postorder(node):
    stack = []
    traversal = []

    stack.append(node)
    while stack:
        current_node = stack.pop()
        traversal.append(current_node)

        if current_node.left is not None:
            stack.append(current_node.left)
        if current_node.right is not None:
            stack.append(current_node.right)

    while traversal:
        current_node = traversal.pop()
        print(current_node.val, end=" ")


preorder(root)
print()
inorder(root)
print()
postorder(root)
print()
