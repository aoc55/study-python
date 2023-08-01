"""
    병합정렬 (재귀 활용)
"""


from typing import MutableSequence


def merge_sort(arr: MutableSequence) -> None:

    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:

        if left < right:

            center = (left + right) // 2
            _merge_sort(a, left, center)
            _merge_sort(a, center + 1, right)

            # Merge 시작
            p = j = 0
            i = k = left

            # Left ~ Center -> Buff 로 임시 복사
            while i <= center:
                buff[p] = a[i]
                i += 1
                p += 1

            # Buff(0~Center) vs a(Centner~Right) 비교 => a 의 앞에서부터 작은 수 채워가기
            while (j < p) and (i <= right):

                if buff[j] < a[i]:  # buff 내 값이 더 작은 경우
                    a[k] = buff[j]
                    j += 1
                    k += 1

                else:  # a 내 값이 더 작은 경우
                    a[k] = a[i]
                    i += 1
                    k += 1

            # 나머지 정리 (Buff 만 수행하면 됨)
            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1

    n = len(arr)
    buff = [None] * n
    _merge_sort(arr, 0, n - 1)
    del buff


if __name__ == '__main__':
    arr = [5, 6, 4, 8, 3, 7, 9, 0, 1, 5, 2, 3]
    merge_sort(arr)
    print(arr)

