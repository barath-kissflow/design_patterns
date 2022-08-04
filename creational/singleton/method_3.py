# Created by Barath M at 04/08/22


__author__ = "Barath M"


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):
    pass


if __name__ == '__main__':
    a = Logger()
    b = Logger()
    print(a is b)
