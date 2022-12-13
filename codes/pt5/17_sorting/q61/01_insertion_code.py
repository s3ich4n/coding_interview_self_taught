from typing import List


def to_swap(n1: int, n2: int) -> bool:
    return str(n1) + str(n2) < str(n2) + str(n1)


def largest_number(nums: List[int]) -> str:
    i = 1

    while i < len(nums):
        j = i
        while j > 0 and to_swap(nums[j - 1], nums[j]):
            # 제자리 정렬이 가능!
            # 공간복잡도 O(1). 다른거 안쓰니까
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1

        i += 1

    # 리턴 결과를 int로 바꿔서 0이 표현되는 케이스를 처리해줌
    return str(int(''.join(map(str, nums))))


test1 = [3, 30, 34, 5, 9]

print(largest_number(test1))
