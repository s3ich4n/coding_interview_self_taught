from typing import List


def three_way_partition(
    a: List[int],
    mid: int,
):
    red = 0
    white = 0
    blue = len(a)

    while white < blue:
        if a[white] < mid:
            a[red], a[white] = a[white], a[red]
            red += 1
            white += 1
        elif a[white] > mid:
            blue -= 1
            a[white], a[blue] = a[blue], a[white]
        else:
            white += 1


q1 = [2, 0, 2, 1, 1, 0]
three_way_partition(q1, mid=1)
print(q1)