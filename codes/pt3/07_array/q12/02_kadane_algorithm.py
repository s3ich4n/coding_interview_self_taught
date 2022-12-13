import sys

from typing import *


def max_profit(prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit


test = [7, 1, 5, 3, 6, 4]
print(max_profit(test))
