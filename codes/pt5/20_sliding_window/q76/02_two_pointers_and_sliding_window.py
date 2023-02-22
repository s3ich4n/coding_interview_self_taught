import collections

from typing import List


def min_window(s: str, t: str) -> str:
    need = collections.Counter(t)
    missing = len(t)
    left = start = end = 0

    # 우측 포인터 판단
    for right, char in enumerate(s, 1):
        # 값이 있는지 (ABC) 보고 있으면 missing을 카운트.
        # 알파벳도 카운트
        missing -= need[char] > 0
        need[char] -= 1

        # 필요한 문자가 0이면 좌측 포인터 판단
        if missing == 0:
            # 불필요한 문자를 가리키고 있는지 확인.
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1

            # 더 작은 값이 있는지 찾아본다.
            if not end or right - left <= end - start:
                # 찾은 값에 대해 정답으로 간주.
                # start, end는 그 의미
                start, end = left, right

            need[s[left]] += 1
            missing += 1
            left += 1

    return s[start:end]


S = "ADOBECODEBANC"
T = "ABC"
print(min_window(s=S, t=T))
