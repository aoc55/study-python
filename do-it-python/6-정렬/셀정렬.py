"""
    셀 정렬
    (단순 삽입 정렬의 개선판)
"""


from typing import MutableSequence


def shell_sort(a: MutableSequence) -> None:
    n = len(a)
    h = 1

    # h - 정렬에서 h 의 최대 값 구하기
    while h < n // 9:
        h = h * 3 + 1

    while h > 0:  # 1 이하면 종료

        # 아래 부분은 삽입정렬과 동일한데 간격이 h 만큼 비교
        for i in range(h, n):
            j = i
            temp = a[i]
            while (j > 0) and (a[j-h] > temp):
                a[j] = a[j-h]
                j -= h
            a[j] = temp
        h //= 3     # 3으로 나눈 나머지


if __name__ == '__main__':
    arr = [8, 1, 4, 2, 7, 6, 3, 5]
    shell_sort(arr)
    print(arr)

