"""
    단순 선택 정렬 (Straight Selection Sort)
"""


from typing import MutableSequence


def selection_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n):
        min_idx = i
        # 최소 값(인덱스) 찾기
        for j in range(i + 1, n):
            if a[min_idx] > a[j]:
                min_idx = j
        # Swap
        temp = a[i]
        a[i] = a[min_idx]
        a[min_idx] = temp

if __name__ == '__main__':
    arr = [3, 1, 9, 2, 10]
    selection_sort(arr)
    print(arr)
