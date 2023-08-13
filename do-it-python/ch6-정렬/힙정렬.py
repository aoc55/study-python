"""
    힙 정렬 구현
    - 힙의 자료구조는 배열로 사용
    - 힙은 Value 부모 > 자식으로 구성
    - 정렬은 오름차순
    - 힙을 구성하는 down_heap 메서드, 힙소트를 수행하는 heap_sort 메서드가 핵심
"""


from typing import MutableSequence


# Root Idx 에 위치한 Value 를 적합한 위치로 찾아주기
def down_heap(a: MutableSequence, left: int, right: int) -> None:

    # print(f'downheap 호출 {left}, {right}')
    temp = a[left]
    parent_idx = left

    while parent_idx < (right + 1) // 2:

        # Child 좌 & 우 중 -> 큰 값 찾기
        child_left_idx = (parent_idx * 2) + 1
        child_right_idx = child_left_idx + 1

        child_big_idx = child_right_idx if (child_right_idx <= right) and (a[child_right_idx] > a[child_left_idx]) else child_left_idx  # Left 만 있을때를 대비한 예외처리 포함


        if temp > a[child_big_idx]: # 이미 할 필요 없음
            break
        else:
            a[parent_idx] = a[child_big_idx]  # 값 위로 올림
            parent_idx = child_big_idx # 인덱스 낮춤

    a[parent_idx] = temp


def heap_sort(a: MutableSequence) -> None:

    n = len(a)

    # 최초 힙부터 구성 (down_heap 밑에서부터 수행하면서 위로 올라감)
    for i in range(n-1, -1, -1):  # 9,8,7, .... 0 ..
        down_heap(a, i, n-1)

    # Sorting 수행
    # 1. Root Node 값 추출해서 맨 뒤와 변경
    # 2. 기존 맨 뒤 값을 Root 로 시작해서 다시 heap 구성 (down_heap) -> 이때 범위는 뒤에서 -1 한칸으로 한정
    # 3. 다시 1로 이동

    for i in range((n-1), -1, -1):
        a[0], a[i] = a[i], a[0]     # Root <-> 마지막 node Swap
        down_heap(a, 0, i-1)        # -1 한칸으로 한정해서 다시 heap 구성


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    heap_sort(arr)
    print(f'힙소트 수행결과 = {arr}')
