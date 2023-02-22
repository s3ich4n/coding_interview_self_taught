def hamming_weight(n: int) -> int:
    count = 0

    while n:
        n &= n - 1
        count += 1

    return count


q1 = 0b00000110010001000110000000001011
q2 = 0b00000000000000000000000010000000

print(hamming_weight(q1))
print(hamming_weight(q2))
