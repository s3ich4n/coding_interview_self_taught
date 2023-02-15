#
# 정렬된 값이라 쓸 수 있었던 점에 유의하기!
#


from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) -1

    while not left == right:
        if numbers[left] + numbers[right] < target:
            left += 1
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            return left + 1, right + 1


numbers = [2, 7, 11, 15]
target = 9
print(two_sum(numbers, target))
