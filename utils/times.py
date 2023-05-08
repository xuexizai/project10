import time
from datetime import datetime
from functools import wraps
def nowtime():
    return datetime.now()

def st_time(times):
    return times.strftime('%Y%m%d%H%M%S')
def sleep(seconds=2):
    time.sleep(seconds)
def func_times(func):
    @wraps(func)
    #避免原函数名称变为wrapper
    def wrapper(*args,**kwargs):
        start=time.time()
        print(func())
        end=time.time()
        print(f"{func.__name__}'s running_time is {start-end}")
        return func
    return wrapper
#装饰器，将旧函数变为新函数wrapper
if __name__ == '__main__':
    print(st_time(datetime.now()))
