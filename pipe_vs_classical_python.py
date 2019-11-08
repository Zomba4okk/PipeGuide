from datetime import datetime
from functools import reduce
from itertools import takewhile
from pipe import select, where, take_while, add, Pipe


def func_duration_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        print('Duration: {}'.format(datetime.now() - start_time))
        return result
    return wrapper

'''
Task:
x is a multiple of 27 in the range 0 to 20,000,000. Sum all x * x% 32 until x * x% 32 exceeds 7,000,000.
'''

@func_duration_decorator
def classical_python_algorithm():
    result = 0
    for number in range(1, 20000000):
        if number%27 == 0:
            num_for_sum = number*(number%32)
            if num_for_sum < 7000000:
                    result += num_for_sum
            else:
                break
    return result

@func_duration_decorator
def short_python_algorithm():
    result = reduce(lambda x, y: x+y*(y%32), (0,)+tuple(takewhile(lambda x: x*(x%32)<7000000, filter(lambda x: x%27==0, range(1, 20000000)))))
    return result

@func_duration_decorator
def algorithm_with_pipes():
    elements = range(1,20000000) | where(lambda x: x%27==0) | select(lambda x: x*(x%32)) | take_while(lambda x: x < 7000000)
    return sum(elements)


#################################################
@Pipe
def custom_filter(iterable):
    for number in range(1, 20000000):
        if number%27 == 0:
            num_for_sum = number*(number%32)
            if num_for_sum < 7000000:
                    yield num_for_sum
            else:
                break

@func_duration_decorator
def algorithm_with_custom_pipe(sequense):
    return sum(sequense | custom_filter)
#################################################


if __name__ == '__main__':
    print('Classical algorithm: ')
    result_classic = classical_python_algorithm()
    print('Short algorithm: ')
    result_short = short_python_algorithm()
    print('Algorithm with pipes: ')
    result_pipe = algorithm_with_pipes()
    print('Algorithm with custom pipe: ')
    result_custom_pipe = algorithm_with_custom_pipe(range(1,20000000))
    print('\nAre result equal?\n{}'.format(result_classic==result_short==result_pipe==result_custom_pipe))
