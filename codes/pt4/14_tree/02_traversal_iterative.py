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
    """ 후위순회, 메모리 두배로 쓰기

    traversal을 기록하고 그거대로 찍기

    훨씬 직관적이긴 함
    """
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


def postorder2(node):
    """ 후위순회, 메모리 두배로 쓰고 루프 한번만에 끝내기

    알면 똑똑하다하고 감탄하고 쓸 수 있음.

    https://www.geeksforgeeks.org/iterative-postorder-traversal-using-stack/
    """
    stack = []
    current_node = node

    while True:
        while current_node:
            # 후에 있을 right 순회때문에 두번 넣는다.
            stack.append(current_node)
            stack.append(current_node)
            current_node = current_node.left

        if len(stack) == 0:
            return

        current_node = stack.pop()

        # 우측 순회를 위한 로직.
        # 1.
        #   두번 넣은 이유
        #   한번 current node와 같으면 right쪽을 순회하고
        #   두번째는 자신의 값을 출력하고 None으로 바꿔서 pop 후
        #   스택에 쌓은대로 가기 위함이다
        #
        # 2.
        #   len(stack) > 0은
        #   stack[-1]이 IndexError 뜨는 맨 마지막 순회를 잡기 위함이다
        if (len(stack) > 0 and stack[-1] == current_node):
            current_node = current_node.right

        else:
            print(current_node.val, end=" ")
            current_node = None


preorder(root)
print()
inorder(root)
print()
postorder(root)
print()
postorder2(root)
print()
