import dis


def foo():
    a, b, c = 1, 2, 3

    a, b = c, a
    c = b


def bar():
    a, b, c = 1, 2, 3

    a, b, c = c, a, b
    c = b


dis.dis(foo)
dis.dis(bar)

"""
  5           0 LOAD_CONST               1 ((1, 2, 3))
              2 UNPACK_SEQUENCE          3
              4 STORE_FAST               0 (a)
              6 STORE_FAST               1 (b)
              8 STORE_FAST               2 (c)
             10 LOAD_CONST               0 (None)
             12 RETURN_VALUE
"""
