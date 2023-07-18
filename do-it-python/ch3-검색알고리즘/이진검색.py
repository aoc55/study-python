from typing import Any, Sequence

"""
    보초법
"""


def bin_search(a: Sequence, key: Any) -> int:
    pl = 0
    pr = len(a) - 1

    while True:
        pc = (pl + pr) // 2

        if a[pc] == key:    # 가운데
            return pc
        elif a[pc] < key:  # 오른쪽
            pl = pc + 1
        else:
            pr = pc - 1     # 왼쪽

        if pl > pr:
            break

    return -1


if __name__ == '__main__':
    arr = [1, 2, 3, 5, 7, 8, 9]
    print(bin_search(arr, 5))
    print(bin_search(arr, 3))
    print(bin_search(arr, 9))
    print(bin_search(arr, 6))

