import bisect

from typing import List, Set


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    result: Set = set()

    nums1.sort()
    nums2.sort()

    i = j = 0

    # 값이 작은 쪽 포인터가 우측으로 가면서 똑같은지 체크
    while i < len(nums1) and j < len(nums2):
        # nums1 쪽이 더 큰 경우
        if nums1[i] > nums2[j]:
            j += 1

        # nums2 쪽이 더 큰 경우
        elif nums1[i] < nums2[j]:
            i += 1
        # 같은 경우
        else:
            result.add(nums1[i])
            i += 1
            j += 1


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersection(nums1, nums2))
