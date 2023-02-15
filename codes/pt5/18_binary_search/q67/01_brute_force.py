from typing import List, Set


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    result: Set = set()

    for n1 in nums1:
        for n2 in nums2:
            if n1 == n2:
                result.add(n1)

    return result


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersection(nums1, nums2))
