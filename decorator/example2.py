from functools import wraps

class Decorator:
    """
    函数调用计数装饰器
    """
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

@Decorator
def sum_func(a, b):
    return a + b

if __name__ == '__main__':
    for i in range(0, 10):
        print(sum_func(i, i))
    print(sum_func.count)