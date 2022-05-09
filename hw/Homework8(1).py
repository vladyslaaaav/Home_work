def decorator(func):
    """Напишіть декоратор, який перетворює всі вхідні параметри функції в строки (str),
     а також перетворює результат роботи функції на строку"""
    def foo(*args):
        for arg in args:
            if not isinstance(args, str):
                print(str(arg))
            result = func(*args)
        return result
    return foo

@decorator
def some(a):
    return str(a)

print(some(3))
