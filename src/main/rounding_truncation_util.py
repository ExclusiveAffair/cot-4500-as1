import math

def my_truncate(number, digits):
    step = 10.0 ** digits
    return math.trunc(step * number) / step

def my_round(number, digits):
    return my_truncate(number + (5 * (0.1 ** (digits + 1))), digits)