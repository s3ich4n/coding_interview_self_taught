import collections


class Solution:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)

        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0


a = Solution()
a.push(1)
a.push(2)
a.push(3)
a.push(4)

print(a.pop())
print(a.pop())

print(a.top())

print(a.empty())
