class BinaryHeap:
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    def _percolate_up(self):
        i = len(self)
        parent = i // 2
        while parent > 0:
            # 부모보다 작으면
            if self.items[i] < self.items[parent]:
                # swap
                self.items[parent], self.items[i] = \
                    self.items[i], self.items[parent]
            i = parent
            parent = i // 2

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def _percolate_down(self, idx):
        """ 다운힙 연산에 대한 로직

        인덱스가 교체되었다면 서로 값을 스왑하고 재귀호출.
        스왑되지 않을 때 까지 자식노드로 계속 내려가며 스왑.

        다시말해 힙 특성이 유지될 때 까지 반복호출.
        """
        left = idx * 2
        right = (idx * 2) + 1
        smallest = idx

        # 왼쪽값 비교
        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left

        # 오른쪽값 비교
        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right

        if smallest != idx:
            self.items[idx], self.items[smallest] = \
                self.items[smallest], self.items[idx]
            self._percolate_down(smallest)

    def extract(self):
        extracted = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self._percolate_down(1)

        return extracted


b = BinaryHeap()

# 삽입
b.insert(5)
b.insert(9)
b.insert(17)
b.insert(27)
b.insert(11)
b.insert(14)
b.insert(21)
b.insert(33)
b.insert(19)
b.insert(18)
print(b.items)
print()


# 추출
for _ in range(5):
    print(f"popped: {b.extract()}", end=' ')
    print(f"\tremained: {b.items}")
