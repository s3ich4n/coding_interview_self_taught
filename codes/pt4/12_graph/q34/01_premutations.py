from typing import List


def solution(nums: List[list]) -> List[List[int]]:
    results = []
    prev_elements = []

    def dfs(elements):
        # 리프 노드면 결과를 추가하기.
        if len(elements) == 0:
            # 현재까지의 값에 대한 참조값을 results에 넣음으로서
            # 모든 갯수를 카운트한다 할 수 있겠다.
            results.append(prev_elements[:])

        # 순열 생성에 대한 재귀호출
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return results


test1 = [1, 2, 3]

solution(test1)
