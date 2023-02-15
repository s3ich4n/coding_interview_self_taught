def search_matrix(
    matrix,
    target,
):
    return any(target in row for row in matrix)


array = [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]

target1 = 5      # True. 값이 있으므로
target2 = 20     # False. 값이 없으므로
print(search_matrix(array, target1))
print(search_matrix(array, target2))
