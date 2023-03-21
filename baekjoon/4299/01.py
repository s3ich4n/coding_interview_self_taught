import sys

a, b = map(int, sys.stdin.readline().split())
two_a_divided_by_2 = (a + b) / 2
if two_a_divided_by_2.is_integer():
    if a - two_a_divided_by_2 < 0:
        print(-1)
    else:
        if int(two_a_divided_by_2) > int(a - two_a_divided_by_2):
            print(f"{int(two_a_divided_by_2)} {int(a - two_a_divided_by_2)}")
        else:
            print(f"{int(a - two_a_divided_by_2)} {int(two_a_divided_by_2)}")
else:
    print(-1)
