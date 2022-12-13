from typing import *


def merge(
        intervals: List[List[int]]
) -> List[List[int]]:
    merged = []

    # 인터벌 내의 값을 하나씩 꺼내고,
    # 첫째값을 키로 하여 정렬을 한번 한 상태
    for idx in sorted(intervals, key=lambda x: x[0]):
        # 맨 끝 리스트의 두 번째 값보다 작으면?
        if merged and idx[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], idx[1])
        else:
            merged += [idx, ]

    return merged


test1 = [[1, 3], [2, 6], [8, 10], [15, 18]]

print(merge(test1))
