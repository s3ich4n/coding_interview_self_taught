def solution(s: str) -> bool:
    stack = []
    table = {
        ")": "(",
        "}": "{",
        "]": "[",
    }

    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False

    # 길이가 0이면 쌍을 다 맞춘 것
    return len(stack) == 0


# test1 = "(){}[]"
# test1 = "({[()]})"
# test1 = "[({()})]"
test1 = "[[[[((()))]]"
print(solution(test1))
