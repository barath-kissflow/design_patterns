# Created by Barath M at 04/08/22


__author__ = "Barath M"


class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Logger, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance


if __name__ == '__main__':
    a = Logger()
    b = Logger()
    print(a is b)
