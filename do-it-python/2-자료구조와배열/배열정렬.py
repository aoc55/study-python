from typing import Any, MutableSequence


# 주어진 배열을 역순으로 정렬하기
def reverse_array(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n // 2):
        a[i], a[n-i-1] = a[n-i-1], a[i]  # Swap


if __name__ == '__main__':
    x = [10, 20, 30, 40, 50]
    reverse_array(x)
    print(x)



