import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: TreeNode) -> str:
        queue = collections.deque([root])
        result = ["#"]

        while queue:
            node = queue.popleft()

            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                result.append("#")

        return ' '.join(result)

    def deserialize(self, data: str) -> TreeNode:
        # 예외처리
        #   이런건 처음부터 구상하면 좋겠지만, 일단 알고리즘부터 익숙해지자
        #   경계값 테스트를 항상 생각하자...
        if data == "# #":
            return None

        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])

        # 0은 비우고, 1은 루트니까 2부터...
        index = 2

        # fast runner처럼, 자식노드결과를 먼저 보고 큐에 추가
        # 비즈니스 로직만 어떻게 녹이느냐이지, BFS는 변함이 없다
        while queue:
            node = queue.popleft()
            if nodes[index] != '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] != '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1

        return root
