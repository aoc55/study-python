"""
    진법 변환 예제
"""


def card_conv(x: int, r: int) -> str :  # x : 정수, r : 희망 진수

    d = ''
    dchar = '01234576890ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0:
        d += dchar[x % r]
        x = x // r

    return d[::-1]  # 역순으로 리턴


if __name__ == '__main__':
    print('10진수 -> N진수 변환기')
    x = int(input('10진수 정수 :'))
    r = int(input('N진수? :'))
    print(card_conv(x, r))
