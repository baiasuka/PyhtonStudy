import threading
import random

uid = random.randint(0, 10)

class ThreadSingleton(object):
    """
    线程安全单例模式的类
    """
    _instance_lock = threading.Lock()

    def __init__(self, *args, **kwargs):
        self.id = uid

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with ThreadSingleton._instance_lock:
                if not hasattr(cls, '_instance'):
                    ThreadSingleton._instance = super().__new__(cls)
                    print("create_new")

        return ThreadSingleton._instance

    def conn(self):
        return self.id


class Connnetion(object):
    """
    普通类
    """
    def __init__(self):
        self.id = uid

    def conn(self):
        return self.id