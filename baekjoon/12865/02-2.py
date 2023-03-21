import sys


class ZeroOneKnapsack:

    def __init__(
            self,
            max_val,
            len_val,
            weights,
            values,
    ) -> None:
        self.len_val = len_val
        self.max_val = max_val
        self.weights = weights
        self.values = values
        self.S = [
            [0 for _ in range(max_val + 1)]
            for _ in range(len_val + 1)
        ]

    def solve(self):

        for i in range(1, self.len_val + 1):
            for j in range(1, self.max_val + 1):
                small = self.S[i - 1][j]
                curr_val = 0

                if self.weights[i - 1] <= j:
                    curr_val = self.values[i - 1] + self.S[i-1][j - self.weights[i - 1]]

                self.S[i][j] = max(small, curr_val)

        return self.S[-1][-1]


if __name__ == "__main__":
    items = []
    values = []

    num_of_items, max_size = map(int, sys.stdin.readline().split())
    for _ in range(num_of_items):
        item, value = map(int, sys.stdin.readline().split())
        items.append(item)
        values.append(value)

    solution = ZeroOneKnapsack(max_size, num_of_items, items, values)

    print(solution.solve())
