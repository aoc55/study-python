"""
    재귀를 활용한 유클리드 호제법
    최대공약수 GCD(X, Y) 구하기
"""


def gcd(x: int, y: int) -> int:
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


if __name__ == '__main__':
    print(gcd(10, 8))
