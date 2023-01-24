from enum import Enum
from rounding_truncation_util import *

class Arith_Type(Enum):
    NONE = 1
    ROUND = 2
    TRUNCATE = 3

DOUBLE_PRECISION = 64
ROUNDING_VAL = 3

def pad_end(value):
    while len(value) < DOUBLE_PRECISION:
        value += "0"
    return value

def get_double_precision_val(str, arithmetic_type):
    exponent = get_double_precision_val_helper(str[1:12], False) - 1023
    mantissa = get_double_precision_val_helper(str[12:], True, arithmetic_type) + 1
    sign = -1 if (str[0] == '1') else 1

    return sign * pow(2, exponent) * mantissa

def get_double_precision_val_helper(str, is_float_component, arithmetic_type = Arith_Type.NONE):
    res = 0
    
    # convert this floating point binary string to base 10
    if (is_float_component):
        pow = 0.5
        for c in str:
            if (c == '1'): res += pow
            pow *= 0.5
            if arithmetic_type == Arith_Type.ROUND:
                pow = my_round(pow, ROUNDING_VAL)
            elif arithmetic_type == Arith_Type.TRUNCATE:
                pow = my_truncate(pow, ROUNDING_VAL)
            
    # convert this integer binary string to base 10
    else:
        pow = 1
        for c in str[::-1]:
            if (c == '1'): res += pow
            pow *= 2
            
    return res    
