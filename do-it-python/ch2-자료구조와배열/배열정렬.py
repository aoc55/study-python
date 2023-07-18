from typing import Any, MutableSequence


# 주어진 배열을 역순 정렬
def reverse_array(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n // 2):  # 최대 N/2번 수행
        a[i], a[n-i-1] = a[n-i-1], a[i]  # Swap


if __name__ == '__main__':

    '''
        역순으로 정렬하기
    '''
    # 직접 정의한 함수 활용한 역순 정렬
    x = [10, 20, 30, 40, 50]
    reverse_array(x)
    print(x)

    # 파이썬 라이브러리 활용한 역순 정렬 (1)
    y = [10, 20, 30, 40, 50]
    y.reverse()
    print(y)

    # 파이썬 라이브러리 활용한 역순 정렬 (2)
    z = [10, 20, 30, 40, 50]
    print(list(reversed(z)))




