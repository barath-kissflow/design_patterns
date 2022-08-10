# Created by Barath M at 10/08/22


__author__ = "Barath M"

from datetime import datetime
import time


def log_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.utcnow()
        result = func(*args, **kwargs)
        print("-------- Time taken to execute %s: %s --------" %
              (func.__name__, (datetime.utcnow() - start_time)))
        return result

    return wrapper


@log_time
def get_data():
    print('fetching records....')
    time.sleep(2)


if __name__ == '__main__':
    get_data()
