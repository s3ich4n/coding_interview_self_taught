from typing import List


def utf8(data: List[int]) -> bool:
    # 문자 앞이 0b10 으로 시작하는지 확인하는 로직
    def check(size: int):
        for i in range(start + 1, start + size + 1):
            if i >= len(data) or (data[i] >> 6) != 0b10:
                return False

        return True

    start = 0
    while start < len(data):
        first = data[start]

        if (first >> 3) == 0b11110 and check(3):
            start += 4
        
        if (first >> 4) == 0b1110 and check(2):
            start += 3

        if (first >> 5) == 0b110 and check(1):
            start += 2

        if (first >> 7) == 0:
            start += 1

        else:
            return False

    return True


data1 = [197, 130, 1]
data2 = [235, 140, 4]

print(utf8(data1))
print(utf8(data2))
