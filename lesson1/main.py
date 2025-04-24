# 1
import datetime


def decorator_run_time(func):
    def inner():
        now1 = datetime.datetime.now()
        func()
        now2 = datetime.datetime.now()
        return now2 - now1

    return inner


@decorator_run_time
def run1():
    for _ in range(100):
        for _ in range(500):
            pass


@decorator_run_time
def run2():
    for _ in range(1000):
        pass


print(run1())
print(run2())

# 2
dic = {}


def decor(func):
    def inner(n):
        if dic.keys().__contains__(n):
            return dic[n]
        else:
            num = func(n)
            dic[n] = num
            return num

    return inner


@decor
def calc_fib(n):
    num1 = 0
    num2 = 1
    for _ in range(n - 1):
        num3 = num1 + num2
        num1 = num2
        num2 = num3
    return num2


def invite():
    for i in range(9):
        print(calc_fib(i))
    print(calc_fib(8))


invite()
