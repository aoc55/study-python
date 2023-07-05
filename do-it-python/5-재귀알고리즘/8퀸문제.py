"""
    8퀸 문제
    - 재귀를 활용
    - 핵심은 Branching (분기) + Bounding (한정) => Branching & Bounding Method (분기한정법)
"""


pos = [0] * 8           # 각 열에 위치한 퀸의 위치 (index : 열, value : 행)
flag_a = [False] * 8    # 각 행에 퀸을 이미 비치했는지 체크용
flag_b = [False] * 15   # 대각선에 퀸을 이미 비치했는지 체크용 (8x8 테이블에서 대각선은 총 15개)
flag_c = [False] * 15   # 반대 대각선에 퀸을 이미 비치했는지 체크용 (8x8 테이블에서 대각선은 총 15개)


def set_queen(i: int) -> None:
    for j in range(8):      # j -> 행 위치 (Branching)
        if (not flag_a[j]) and (not flag_b[i+j]) and (not flag_c[i-j+7]):   # flag 체크 (Bounding)

            pos[i] = j  # i열의 j행에 퀸 배치

            if i == 7:
                put()
            else:
                flag_a[j] = True
                flag_b[i + j] = True
                flag_c[i - j + 7] = True

                set_queen(i + 1)

                flag_a[j] = False
                flag_b[i + j] = False
                flag_c[i - j + 7] = False


def put() -> None:
    print('--------')
    # 각 열에 배치한 퀸의 위치 출력
    for j in range(8):
        for i in range(8):
            if pos[i] == j:
                print('Q', end='')
            else:
                print('X', end='')
        print('')
    print('--------')


if __name__ == '__main__':
    set_queen(0)    # 시작