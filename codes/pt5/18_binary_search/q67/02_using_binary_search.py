import bisect

from typing import List, Set


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    result: Set = set()

    nums2.sort()

    for n1 in nums1:
        i2 = bisect.bisect_left(nums2, n1)
        #
        # 1. len(nums2) > 0으로 예외처리
        # 2. len(nums2) > i2로 인덱스를 찾았나 체크
        # 3. n1 == nums2[i2] 로 값이 같은지 체크
        #
        if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
            result.add(n1)

    return result


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersection(nums1, nums2))
