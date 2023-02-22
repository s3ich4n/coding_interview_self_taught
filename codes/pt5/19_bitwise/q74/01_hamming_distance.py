def count_of_1(n: int) -> int:
    return bin(n ^ 0).count('1')


q1 = 0b00000000000000000000000000001011
q2 = 0b00000000000000000000000010000000

print(count_of_1(q1))
print(count_of_1(q2))
