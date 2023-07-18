"""
    Bubble Sorting
    v1 -> 뒤에서부터 정렬하는 방식
    v2 -> 앞에서부터 정렬하는 방식
    v3 -> v2 기반 개선된 방식 (조기탈출 조건추가)
          한사이클 돌려서 Swap 횟수가 0 이면 -> 이미 정렬이 완료되었음을 활용
    v4 -> v2 기반 개선된 방식 (스캔 범위 제한하기)
          직전 사이클에서 swap 이 이루어졌던 영역까지만 다음 사이클에서 수행
"""


from typing import MutableSequence


def bubble_sort_v1(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if a[j-1] > a[j]:
                temp = a[j-1]
                a[j-1] = a[j]
                a[j] = temp


def bubble_sort_v2(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                temp = a[j+1]
                a[j+1] = a[j]
                a[j] = temp


def bubble_sort_v3_advanced(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n-1):
        swap_count = 0
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                temp = a[j+1]
                a[j+1] = a[j]
                a[j] = temp
                swap_count += 1
        if swap_count == 0:
            print(f'[{i}번째] swap count = 0, 배열이 모두 정렬되어 있음')
            break


def bubble_sort_v4_advanced(a: MutableSequence) -> None:
    n = len(a)
    k = n-1
    while k > 0:
        last = 0    # 중요 (Swap 이 한번도 안 이루어질 경우 탈출조건)
        for j in range(k):
            if a[j] > a[j+1]:
                temp = a[j+1]
                a[j+1] = a[j]
                a[j] = temp
                last = j
        k = last
        print(a, k)


if __name__ == '__main__':
    arr = [10, 5, 30, 2, 8]
    bubble_sort_v1(arr)
    print(arr)
    print('')

    arr2 = [10, 5, 1, 30, 2, 8, 7, 15]
    bubble_sort_v2(arr2)
    print(arr2)
    print('')

    arr3 = [10, 5, 1, 30, 2, 8, 7, 15]
    bubble_sort_v3_advanced(arr3)
    print(arr3)
    print('')

    arr4 = [1, 2, 3, 4]
    bubble_sort_v3_advanced(arr4)
    print(arr4)
    print('')

    arr5 = [10, 5, 1, 30, 2, 8, 7, 15]
    bubble_sort_v4_advanced(arr5)
    print(arr5)
    print('')
