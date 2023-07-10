"""
    셰이커 정렬
    - 버블소트의 개선판
    - 양방향 버블 소트
    - 칵테일 정렬
"""


from typing import MutableSequence


# 일반 Bubble Sort
def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    count = 0
    for i in range(n - 1):
        for j in range(n -1, i, -1):
            if a[j-1] > a[j]:
                temp = a[j-1]
                a[j-1] = a[j]
                a[j] = temp
        count += 1
    print(f'Bubble Sort = {count}')


# Shaker Sort
def shaker_sort(a: MutableSequence) -> None:
    count = 0
    left = 0
    right = len(a) - 1
    last = right
    while left < right:
        # 뒤에서 시작
        for j in range(right, left, -1):
            if a[j-1] > a[j]:
                temp = a[j-1]
                a[j-1] = a[j]
                a[j] = temp
                last = j
        left = last
        count += 1

        # 앞에서 시작
        for j in range(left, right):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                last = j
        right = last
        count += 1
    print(f'Shaker Sort = {count}')


if __name__ == '__main__':
    arr = [9, 1, 3, 4, 6, 7, 8]
    bubble_sort(arr)
    print(arr)

    arr2 = [9, 1, 3, 4, 6, 7, 8]
    shaker_sort(arr)
    print(arr)
