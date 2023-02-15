def search_matrix(
    matrix,
    target,
):
    if not matrix:
        return False
    
    # 첫째 행의 맨 뒤
    row = 0
    col = len(matrix[0]) - 1

    while row <= len(matrix) - 1 and col >= 0:
        if target == matrix[row][col]:
            return True

        elif target < matrix[row][col]:
            col -= 1
        
        elif target > matrix[row][col]:
            row += 1
        
        else:
            AssertionError("logic error")
    
    return False


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
