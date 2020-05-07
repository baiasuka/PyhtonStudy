# 用类实现的带参数的装饰器及两个装饰器叠加示例
from functools import wraps


class decoratorA:
    def __init__(self, on=True):
        self._on = on

    def __call__(self, func):
        @wraps(func)
        def _wrapperA(*args, **kwargs):
            print("check permission on")
            if kwargs["user"] == 'hong':
                print("it's hong")
                return func(*args, **kwargs)
            else:
                return 'no permission'

        @wraps(func)
        def _wrapperB(*args, **kwargs):
            print("check permission off")
            return func(*args, **kwargs)

        if self._on:
            return _wrapperA
        else:
            return _wrapperB


def decoratorB(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs["user"] in ["hong", "xiao"]:
            print("is hostage")
            return func(*args, **kwargs)
        else:
            print("is not hostage")
            return func(*args, **kwargs)
    return wrapper


@decoratorB
@decoratorA(on=True)
def funcionA(a, b, user):
    print("user:"+str(user)+" sum a + b = "+str(a + b))
    return a + b


print(funcionA(a=3, b=6, user='hou'))