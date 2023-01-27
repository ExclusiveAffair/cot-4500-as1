from binary_to_decimal_util import *
from abs_rel_error_util import *
from convergence_util import *
from root_finding_util import *

if __name__ == "__main__":
    
    # see binary_to_decimal_util.py
    exercise_1_str = pad_end("010000000111111010111001")
    exercise_1_val = get_double_precision_val(exercise_1_str)
    print('%.5f\n' % exercise_1_val)

    truncated = my_truncate(exercise_1_val, 3)
    rounded = my_round(exercise_1_val, 3)
    print(truncated, '\n')
    print(rounded, '\n')

    # see abs_rel_error_util.py
    print(absolute_error(exercise_1_val, rounded))
    print(relative_error(exercise_1_val, rounded), '\n')

    # see convergence_util.py
    print(min_term_error(1), '\n')

    # see root_finding_util.py
    print(bisection_method(-4, 7), '\n')
    print(newton_raphson_method(7))
