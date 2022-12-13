from typing import *


def sum_of_three(
        nums: List[int],
) -> List[List[int]]:
    results = []

    # 일단 정렬
    nums.sort()

    # n^3 brute force
    for i in range(len(nums) - 2):
        # 숫자가 같은 경우엔 굳이 루프를 돌 필요가 없겠죠?
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 1):
            # 숫자가 같은 경우엔 굳이 루프를 돌 필요가 없겠죠?
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, len(nums)):
                # 숫자가 같은 경우엔 굳이 루프를 돌 필요가 없겠죠?
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append([nums[i], nums[j], nums[k]])

    return results


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, 4]

    print(sum_of_three(nums))
