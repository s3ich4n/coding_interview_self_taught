import decimal
import sys


a, b = map(str, sys.stdin.readline().split())
print(decimal.Decimal(a) / decimal.Decimal(b))
