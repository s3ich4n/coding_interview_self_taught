from typing import *


def trap(
        height: List[int]
) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        # 변곡점을 만날 때
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()

            if not len(stack):
                break

            # 이전과의 차이만큼 물높이를 처리한다
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        stack.append(i)

    return volume


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    print(trap(height))
