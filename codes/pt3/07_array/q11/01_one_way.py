from typing import List


def product_except_self(
        nums: List[int]
) -> List[int]:
    output = []

    p = 1
    for i in range(0, len(nums)):
        output.append(p)
        p = p * nums[i]

    p = 1
    for i in range(len(nums) - 1, 0 - 1, -1):
        output[i] = output[i] * p
        p = p * nums[i]

    return output


test = [1, 2, 3, 4]
print(product_except_self(test))
