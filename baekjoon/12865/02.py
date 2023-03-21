import sys


class ZeroOneKnapsack:

    def __init__(
            self,
            max_val,
            len_val,
            weights,
            values,
    ) -> None:
        self.max_val = max_val
        self.len_val = len_val
        self.weights = weights
        self.values = values

    def solve(self):

        return self._knapsack(
            self.max_val,
            self.len_val,
            self.weights,
            self.values,
        )

    def _knapsack(
            self,
            max_val,
            len_val,
            weights,
            values,
    ):
        if max_val == 0 or len_val == 0:
            return 0

        if weights[len_val - 1] > max_val:
            return self._knapsack(max_val, len_val - 1, weights, values)
        else:
            n_include = values[len_val - 1] + self._knapsack((max_val - weights[len_val - 1]), len_val - 1, weights, values)  # noqa
            n_exclude = self._knapsack(max_val, len_val - 1, weights, values)
            return max(n_include, n_exclude)


if __name__ == "__main__":
    values = []
    weights = []

    num_of_items, max_size = map(int, sys.stdin.readline().split())
    for _ in range(num_of_items):
        item, value = map(int, sys.stdin.readline().split())
        weights.append(item)
        values.append(value)

    solution = ZeroOneKnapsack(max_size, num_of_items, weights, values)
    print(solution.solve())
