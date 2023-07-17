"""
    퀵소트
"""


from typing import MutableSequence


def partition(a: MutableSequence) -> None:
    n = len(a)
    pl = 0
    pr = n - 1
    x = a[n//2]

    while pl <= pr:

        while a[pl] < x:
            pl += 1
        while a[pr] > x:
            pr -= 1

        if pl <= pr:
            print(f'{pl} <-> {pr}')
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    print(f'Pivot {x}')
    print('Pivot 이하 Group')
    print(*a[0:pl])

    if pl > pr + 1:
        print("Pivot 일치 Group")
        print(*a[pr+1:pl])

    print("Pivot 이상 Group")
    print(*a[pr+1:n])



def qsort(a: MutableSequence, left: int, right:int) -> None:
    pl = left
    pr = right
    x = a[(left + right) // 2]

    while pl <= pr:
        while a[pl] < x:
            pl += 1
        while a[pr] > x:
            pr -= 1

        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr:
        qsort(a, left, pr)
    if right > pl:
        qsort(a, pl, right)


def quick_sort(a: MutableSequence) -> None:
    qsort(a, 0, len(a)-1)



if __name__ == '__main__':
    # arr = [1, 8, 7, 4, 5, 2, 6, 3, 9]
    # arr = [9, 8, 7, 5, 5, 12, 2, 10]
    arr = [3, 10, 9, 4, 15, 5]
    partition(arr)
    # quick_sort(arr)
    print(arr)

