def get_sum(a: int, b: int) -> int:
    """ 32비트 덧셈 구현
    """
    MASK = 0xFFFFFFFF       # 2의 보수를 만들기 위한 값
    INT_MAX = 0x7FFFFFFF

    # a에는 a, b의 합을 넣음
    # b에는 자릿수를 올려가며 carry 값을 담음
    while b != 0:
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

    # 음수 처리
    if a > INT_MAX:
        a = ~(a ^ MASK)

    return a


print(get_sum(-3, 2))
print(get_sum(1, 2))
