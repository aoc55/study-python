# 위치인자 | 키워드 인자
def my_func1(param1, param2, param3):
    print(param1, param2, param3, sep=" | ")


my_func1("가", "나", "다")     # 위치 인자만 사용
my_func1(param3="다", param2="나", param1="가")   # 키워드 인자만 사용
my_func1("가", "나", param3="다")              # 위치 인자 + 키워드 인자 혼합 사용


# *args (위치인자 모으기), **kwargs (키워드 인자 모으기)
def my_func2(param1, param2, *args, **kwargs):
    print(param1, param2, args, kwargs, sep=", ")


my_func2("a", "b")  # a, b, (), {}
my_func2("a", "b", "c", "d")    # a, b, ('c', 'd'), {}
my_func2("a", "b", "c", "d", mykey='가', mykey2='나')   # a, b, ('c', 'd'), {'mykey': '가', 'mykey2': '나'}


# docstring
def my_func3_1():
    """this is docstring sample"""    # 정의 위치
    pass


help(my_func3_1)    # docstring 확인하기
print(my_func3_1.__doc__)   # 서식 없이 docstring 확인하기


# 일급객체 함수
def my_func_4():
    print("this is my_func4")


def my_func_5(func):
    func()      # 전달받은 함수 실행


my_func_5(my_func_4)  # 함수를 파라미터로 전달


# 일급객체 함수2
def my_sum(*args):
    result = sum(args)
    print(f'sum result = {str(result)}')


def run_something_with_args(func, *args):
    func(*args)      # 전달받은 함수 실행


run_something_with_args(my_sum, 10, 20, 30)  # 함수를 파라미터로 전달


# 내부 함수
def outside_func(num):
    def inner_func(num2):
        return num2 * 10
    print(f'result = {inner_func(num)}')


outside_func(10)


# 내부함수의 클로저화
def outside_func_closure(num):
    def inner_func_closure():
        return num * 1000   # 바깥 함수 변수에 직접 참조
    return inner_func_closure   # 반환하는 것은 함수


closure_func = outside_func_closure(100)    # Clousre 함수를 변수에 저장
closure_func2 = outside_func_closure(200)
print(closure_func, closure_func2)
# Closure 함수 실행
print(closure_func())   # 100000
print(closure_func2())  # 200000


# 람다
def num_with_mylambda(num, func):
    result = func(num)
    print(f'result = {result}')


num_with_mylambda(100, lambda x: x // 2)   # 파라미터로 람다 전달해서 실행


# Generator
def range_by_custom_generator(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step


# 만든 Generator 를 List Comprehension 에 사용
print([x for x in range_by_custom_generator()])


# Decorator 직접사용
def my_decorator(func):
    def decorated_func(*args, **kwargs):
        print("==== Decorator Start ====")
        result = func(*args, **kwargs)
        print(f'result = {result}')
        print("==== Decorator End ====")
        return result
    return decorated_func   # Decorated 된 함수를 리턴


def add_ints(a, b):
    return a + b


# Decorated 된 함수 직접 실행
decoratorted_ints = my_decorator(add_ints)
decoratorted_ints(5, 10)


# Decorator 간편사용
@my_decorator
def add_ints_v2(a, b):
    return a + b


add_ints_v2(2, 2)


# Namespace & Scope
global_var = "this is global var"


def local_func():
    global global_var
    global_var = "modified by local_func"


local_func()
print(global_var)


# try ~ Except (#1)
try:
    arr = [1, 2, 3, 4, 5]
    print(arr[100])
except:
    print("error")


# try ~ Except (#2)
try:
    arr = [1, 2, 3, 4, 5]
    print(arr[100])
except IndexError as idxError:
    print(idxError)


# Custom Exception
class MyCustomException(Exception):
    print("this is my Custom Exception")
    pass


# try ~ Except with Custom Exception
try:
    raise MyCustomException()
except MyCustomException as ce:
    print("except custom exception")


# =====
# 연습문제
# =====
print("\n\n ======= 연습문제 ========")

# 4.4
print([x for x in range(10) if x % 2 == 0])
# 4.5
print({k:k*k for k in range(10)})
# 4.6
print({o for o in range(10) if o % 2 == 1})
# 4.7
my_generator = ("Got %s" % x for x in range(10))
for x in my_generator:
    print(x)
# 4.9
my_generator2 = (i for i in range(10) if i % 2 == 1)
for idx, value in enumerate(my_generator2):
    if idx == 2:
        print(f'3번째 -> {value}')
        break

# 4.10


def test(func):
    def do_decorate(*args, **kwargs):
        print("-start-")
        result = func(*args, **kwargs)
        print("-end-")
        return result
    return do_decorate


def minus_int(a, b):
    return a - b


decorated_minus_int = test(minus_int)
print(decorated_minus_int(10, 5))


@test
def minus_int_decorated(a, b):
    return a - b


print(minus_int_decorated(3, 1))