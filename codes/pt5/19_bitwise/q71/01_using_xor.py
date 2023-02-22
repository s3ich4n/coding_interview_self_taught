def hamming_distance(
    x: int,
    y: int,
) -> int:
    return bin(x ^ y).count('1')


print(hamming_distance(1, 4))
