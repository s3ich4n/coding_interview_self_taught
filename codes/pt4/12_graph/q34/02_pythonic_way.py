import itertools


def solution(nums):
    return list(itertools.permutations(nums))


test1 = [1, 2, 3]

print(solution(test1))
