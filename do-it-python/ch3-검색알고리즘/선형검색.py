"""
    초단순 선형검색
    - 정렬되지 않은 배열에서 검색할 때 사용하는 유일한 방법
"""

from typing import Any, Sequence


def seq_search(a: Sequence, key: Any) -> int:
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1


if __name__ == '__main__':
    num = int(input('원소 수 입력: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('검색할 값 입력: '))

    idx = seq_search(x, ky)

    if idx == -1:
        print("미존재")
    else:
        print(f'검색값은 {idx}에 있음')