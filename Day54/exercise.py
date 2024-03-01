import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    function()
    right_now = time.time()
    print(right_now - current_time)


@speed_calc_decorator
def fast_function():
    for i in range(10000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()
