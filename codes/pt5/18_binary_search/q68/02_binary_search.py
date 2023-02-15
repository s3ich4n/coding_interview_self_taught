

from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    for k, v in enumerate(numbers):
        left, right = k + 1, len(numbers) -1

        # 값을 반복하면서 구해놓는다
        expected = target - v

        # 여기서 이진 검색으로 값을 구해서 맞으면 인덱스를 꺼낸다.
        while left <= right:
            mid = left + (right - left) // 2

            if numbers[mid] < expected:
                left = mid + 1

            elif numbers[mid] > expected:
                right = mid - 1
            
            else:
                return k + 1, mid + 1


numbers = [2, 7, 11, 15]
target = 9
print(two_sum(numbers, target))
