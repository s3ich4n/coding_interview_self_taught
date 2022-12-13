from typing import *


def sum_of_three(
        nums: List[int],
) -> List[List[int]]:
    results = []

    # 일단 정렬
    nums.sort()

    for i in range(len(nums) - 2):
        # 중복일 경우에 대한 처리
        # 자기 직전 값과 비교
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # 정답을 찾았으므로, 해당 케이스를 추가
                results.append([nums[i], nums[left], nums[right]])

                # 그 후에는 인덱스를 살펴봄
                #
                # 1) 중복일 경우에 대한 처리
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return results


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, 4]

    print(sum_of_three(nums))
