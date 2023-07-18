"""
    하노이 탑 (재귀)
    - Divide And Conquer ...
"""

# no -> 옮길 원반
# x -> 시작 위치
# y -> 종료 위치
def move(no: int, x: int, y:int) -> None:
    if no > 1:
        move(no - 1, x, 6 - x - y)

    print(f'원반 [{no}]을(를) {x} -> {y}로 옮깁니다')

    if no > 1:
        move(no - 1, 6 - x - y, y)


if __name__ == '__main__':
    move(3, 1, 3)   # 하노이의 탑 호출