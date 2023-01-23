
FUNCTION = "((-1)**k) * (x**k) / (k**3)"
ERROR = 1e-4

def get_kth_term(x, k):
    return eval(FUNCTION)

def check_for_alternating():
    return "(-1)**k" in FUNCTION

def check_for_decreasing(x, iter):
    flag = True
    prev_val = 1e18
    
    for k in range(1, iter):
        result = abs(eval(FUNCTION))

        if prev_val <= result:
            return False

        prev_val = result

    return True

def min_term_error(x):
    if (not check_for_alternating() or not check_for_decreasing(x, 100)):
        return -1

    k = 1

    while abs(get_kth_term(x, k)) > ERROR:
        k += 1

    return k
    