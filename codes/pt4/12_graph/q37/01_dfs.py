from typing import List


def solution(nums: List[int]) -> List[List[int]]:
    result = []

    def dfs(index, path):
        # 매번 결과를 추가한다.
        result.append(path)

        for i in range(index, len(nums)):
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return result


test1 = [1, 2, 3]

print(solution(test1))
