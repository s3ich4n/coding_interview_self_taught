def get_sum(a: int, b: int) -> int:
    """ 32비트 덧셈 구현
    """
    MASK = 0xFFFFFFFF
    INT_MAX = 0x7FFFFFFF

    a_bin = bin(a & MASK)[2:].zfill(32)
    b_bin = bin(b & MASK)[2:].zfill(32)
    
    result = []

    carry = 0
    sum = 0

    for i in range(32):
        A = int(a_bin[31 - i])
        B = int(b_bin[31 - i])

        # 전가산기
        q1 = A & B
        q2 = A ^ B
        q3 = q2 & carry
        sum = carry ^ q2
        carry = q1 | q3

        result.append(str(sum))

    if carry == 1:
        result.append(str(sum))

    # 초과자리수 처리
    result = int(''.join(result[::-1]), base=2) & MASK

    # 음수 처리

    if result > INT_MAX:
        result = ~(result ^ MASK)

    return result


print(get_sum(-3, 2))
print(get_sum(1, 2))
