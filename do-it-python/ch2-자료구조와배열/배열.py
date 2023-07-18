from typing import Any, Sequence
import random

# 배열의 최대 값 구하는 함수
def max_of(a: Sequence) -> Any:  # 함수 애노테이션 달기
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

if __name__ == '__main__':  # 해당 모듈 직접 실행 할때만 동작함

    # print(max_of([1, 2, 3, 10, 5]))
    # print(__name__)

    x = [None] * 10  # Size 10 인 배열 생성
    for i in range(10):
        x[i] = random.randint(10, 100)  # 10 ~ 100 사이의 난수
    print(max_of(x))







