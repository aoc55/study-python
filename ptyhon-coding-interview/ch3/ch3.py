# 제너레이터 만들기
import pprint
def get_natural_number(max_number: int) -> int:
    n = 0
    while n < max_number:
        n += 1
        yield n


def generator():
    yield 1
    yield "abc"
    yield 3.88


if __name__ == '__main__':
    # g = get_natural_number(100)
    # print(type(g))  # <class 'generator'>
    # for _ in range(100):
    #     print(next(g))

    # g = generator()
    # print(next(g))
    # print(next(g))
    # print(next(g))

    # 한줄로 출력
    print('aa', end="")
    print('bb')

    # 리스트 한번에 출력
    a = ['a', 'b']
    print(' '.join(a))

    # 변수 사용 해서 출력
    idx = 1
    fruit = "apple"
    print("{0}: {1}".format(idx, fruit))  # "{0}".format() 사용
    print(f'{idx}: {fruit}')  # f'{변수명}' 사용

    pprint.pprint(locals())







