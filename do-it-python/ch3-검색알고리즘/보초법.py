"""
    보초법 (Sentinel Method)
    - 맨 마지막에 찾으려는 값을 추가
    - IF 기존 배열에 찾는 값이 있다면 ? 맨 마지막까지 가지 않음
    - ELSE 기존 배열에 찾는 값이 없다면 ? 보초까지 이동해서 리턴
    - 즉, "매번 해당 위치가 배열의 마지막인"지에 대한 비교를 할 필요가 없음
    - 효과로 비용 반으로 줄일 수 있음 (매번 i가 배열의 길이를 넘어섰는지에 대한 IF 비교문 불필요!)
"""

from typing import Any, Sequence
import copy


def seq_search(seq: Sequence, key: Any) -> int:
    a = copy.deepcopy(seq)
    a.append(key)   # 보초 추가

    i = 0
    while True:  # i 가 len(seq) 넘어가는지 여부에 대한 별도 계산 필요 없음 !! (if i == len(a) ...)
        if a[i] == key:
            break
        i += 1

    return -1 if i == len(seq) else i  # 절반으로 줄었지만, 1번은 수행해야함


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



