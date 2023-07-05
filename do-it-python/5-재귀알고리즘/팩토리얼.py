"""
    재귀로 구현하는 팩토리얼
"""


def factorial(n: int) -> int:
    if n > 0:
        return factorial(n - 1) * n
    else:
        return 1


if __name__ == '__main__':
    print(factorial(5))
