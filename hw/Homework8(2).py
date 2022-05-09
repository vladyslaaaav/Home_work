import timeit


def time_of_function(func):
    """Напишіть декоратор, який вимірює і виводить на екран час виконання функції в секундах."""
    def wrapper(*args):
        res = func(*args)
        return res
    return wrapper

@time_of_function
def foo(*args):

    print('Hello World')

foo()
print(timeit.timeit())
