from typing import List


def solution(T: List[int]) -> List[int]:
    answer = [0] * len(T)
    stack = []

    for i, cur in enumerate(T):
        # 스택에 값이 있는지? 온도는 직전 인덱스에 비해 높은지?
        while stack and cur > T[stack[-1]]:
            # 상승 지점 스택값의
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)

    return answer


test1 = [73, 74, 75, 71, 69, 72, 76, 73]
print(solution(test1))
