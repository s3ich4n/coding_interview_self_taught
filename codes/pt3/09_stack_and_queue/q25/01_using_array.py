class CircularQueue:
    def __init__(self, k) -> None:
        self.q = [None] * k
        self.maxlen = k
        # 두개의 포인터를 일컫는다.
        self.p1 = 0
        self.p2 = 0

    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            # 앞으로
            self.p2 = (self.p2 + 1) % self.maxlen

            return True
        else:
            # 못넣음
            return False

    def deQueue(self) -> int:
        if self.q[self.p1] is None:
            return False

        else:
            value = self.q[self.p1]
            self.q[self.p1] = None
            # 앞으로
            self.p1 = (self.p1 + 1) % self.maxlen

            return value

    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self) -> int:
        return -1 if self.q[self.q2 - 1] is None else self.q[self.q2 - 1]

    def isEmpty(self) -> bool:
        # 값이 없는 조건
        #   p1, p2가 동일한 위치를 바라봄
        #   p1에 아무값이 없음
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self) -> bool:
        # 꽉찬 조건
        #   p1, p2가 동일한 위치를 바라봄
        #   p1에 값이 있음
        return self.p1 == self.p2 and self.q[self.p1] is not None
