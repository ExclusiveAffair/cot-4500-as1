FUNCTION = "x ** 3 + 4 * (x ** 2) - 10"
DERIVATIVE = "3 * (x ** 2) + 8 * x"
ERROR = 1e-4
MAX_ITERATIONS = 100

def calc_fx(x, f):
    return eval(f)

def bisection_method(a, b):
    iter = 0
    while b - a > ERROR and iter < MAX_ITERATIONS:
        iter += 1
        mid = (b + a) / 2
        if calc_fx(mid, FUNCTION) < 0:
            b = mid
        else:
            a = mid

    return iter

def newton_raphson_method(p0):
    p_prev = p0
    iter = 0
    while iter < MAX_ITERATIONS:
        iter += 1
        f_prime = calc_fx(p_prev, DERIVATIVE)

        if (f_prime != 0):
            p_next = p_prev - calc_fx(p_prev, FUNCTION) / calc_fx(p_prev, DERIVATIVE)
            if abs(p_next - p_prev) < ERROR:
                return iter
            p_prev = p_next
        else:
            return -1

    return iter
