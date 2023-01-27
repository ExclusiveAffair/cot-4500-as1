from enum import Enum
import math

DOUBLE_PRECISION = 64
ROUNDING_VAL = 3

def normalize(number):
    exp = 0
    while abs(number) > 1:
        exp += 1
        number /= 10
    return (number, exp)

def my_truncate(number, digits):    
    if number < 0.1 ** digits:
        return 0

    norm = normalize(number)

    step = 10.0 ** digits
    return (math.trunc(step * norm[0]) / step) * (10 ** norm[1])

def my_round(number, digits):
    norm = normalize(number)
    return my_truncate(norm[0] + (5 * (0.1 ** (digits + 1))), digits)  * (10 ** norm[1])

def pad_end(value):
    while len(value) < DOUBLE_PRECISION:
        value += "0"
    return value

def get_double_precision_val(str):
    exponent = get_double_precision_val_helper(str[1:12], False) - 1023
    mantissa = get_double_precision_val_helper(str[12:], True) + 1
    sign = -1 if (str[0] == '1') else 1

    return sign * pow(2, exponent) * mantissa

def get_double_precision_val_helper(str, is_float_component):
    res = 0
    
    # convert this floating point binary string to base 10
    if (is_float_component):
        iter = 1
        pow = 0.5
        for c in str:
            if (c == '1'): 
                res += pow
            pow *= 0.5
            iter += 1
            
    # convert this integer binary string to base 10
    else:
        pow = 1
        for c in str[::-1]:
            if (c == '1'): res += pow
            pow *= 2
            
    return res    
