# Assignment
# v3.6) 2중 데코레이터 적용. 성능측정 데코레이터, 디스크립션 데코레이터를 팩토리얼 함수에 적용하시오.
import time

def description_decorator(func):
    def wrapper(*arg):
        print(func.__name__)
        print(func.__doc__)
        r = func(*arg)
        return r
    return wrapper


def time_decorator(func):
    def wrapper(*arg):
        s = time.time()
        r = func(*arg)
        e = time.time()
        print(f'실행시간 : {e - s}초')
        return r
    return wrapper

@time_decorator
@description_decorator
def factorial_repetition(n) -> int:
    """
    factorial function by loop
    :param n:
    :return: results of factorial operation
    """
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"function name: {func.__name__}")
        res = func(*args,**kwargs)
        return res
    return wrapper


@log_decorator
def greet(name, greeting="안녕"):
    return f"{name}{greeting}"
# number = int(input())
# print(f"{number}! = {factorial_repetition(number)}")


# number = int(input())
# ft = time_decorator(factorial_repetition)
# print(f"{number}! = {ft(number)}")
# number = int(input())
# print(f"{number}! = {factorial_repetition(number)}")

print(greet("son"))