import collections


class ListNode:
    def __init__(
        self,
        key=None,
        value=None,
    ) -> None:
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self) -> None:
        self.size = 1_000
        self.table = collections.defaultdict(ListNode)

    def put(
        self,
        key: int,
        value: int,
    ) -> None:
        index = key % self.size

        # 인덱스에 아무것도 없으면 키, 값 삽입 후 종료
        # 특이한 점)
        # value의 존재유무를 비교.
        # 테이블이 `defaultdict` 이므로 값이 없으면 기본값을 생성시킴. 그 때문.
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        # 인덱스를 가져온다.
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next

        # 값 대입하고, 새 체이닝을 추가.
        p.next = ListNode(key, value)

    def get(
        self,
        key: int,
    ) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1

        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next

        return -1

    def remove(
        self,
        key: int,
    ) -> None:
        index = key % self.size

        if self.table[index].value is None:
            return

        # 첫 번째 노드일 때 삭제처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
