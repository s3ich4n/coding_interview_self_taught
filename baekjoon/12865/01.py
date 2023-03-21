import sys

item_lists = []
item_weights = []

items, weights = map(int, sys.stdin.readline().split())
for _ in range(items):
    x, y = map(int, sys.stdin.readline().split())
    item_lists.append(x)
    item_weights.append(y)

for x, y in zip(item_weights, item_lists):
    print(f"{x}+{y}={x+y}")
