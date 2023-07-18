"""
    소수 구하기 V1
    - 가장 단순한 방법 ... 그러나 불필요한 연산 추가 발생
    - ex. 2와 3으로 나누어 떨어지지 않는다면 ? 당연히 4(2x2) or 6(2x3) 으로도 나누어 떨어지지 않음
"""


def print_prime_v1() -> None:
    counter = 0  # 연산횟수 기록용
    for n in range(2, 1001):
        for i in range(2, n-1):
            counter += 1
            if n % i == 0:
                break
        else:
            print(n)
    print(f'나눗셈 수행한 결과 : {counter}')  # 77855

# print_prime_v1()


"""
    소수 구하기 V2
    - N이 소수인 경우? 2부터 N-1까지 어떤 소수로 나누어 떨어지지 않음.
    - 이를 활용해서 소수인지 판별하기 위해? '2부터 N-1까지의 범위 내 소수로 나누어지는 경우가 있는지만' 확인하면 됨.
    연산 횟수는 줄으나 -> 소수 배열이라는 메모리를 필요로 함.
"""


def print_prime_v2() -> None:
    counter_v2 = 0  # 나눗셈 횟수
    ptr_v2 = 0
    prime_v2 = [None] * 500  # 소수 저장용 배열

    # 소수 2는 기본 세팅
    prime_v2[ptr_v2] = 2
    ptr_v2 += 1

    for n in range(3, 1001, 2):  # (짝수는 애초에 연산 할 필요없음)
        for i in range(1, ptr_v2):   # 1부터 시작하는 이유? 어차피 N 홀수이기에 prime_v2[0] : 2 는 연산 불필요
            counter_v2 += 1
            if n % prime_v2[i] == 0:
                break
        else:
            prime_v2[ptr_v2] = n
            ptr_v2 += 1

    # 소수 출력
    for i in range(ptr_v2):
        print(prime_v2[i])

    print(f'나눗셈 실행 횟수: {counter_v2}')  # 15121

# print_prime_v2()


"""
    소수 구하기 V3
    - N의 제곱근 이하의 어떤 소수로도 나누어 떨어지지 않으면 소수.
    - 즉, 기존 Ver 2의 경우에서 확장해서 연산 횟수 줄이긴
"""


def print_prime_v3() -> None:
    counter_v3 = 0
    ptr_v3 = 0
    prime_v3 = [None] * 500

    # 소수 2는 기본 세팅
    prime_v3[ptr_v3] = 2
    ptr_v3 += 1

    # 소수 3는 기본 세팅
    prime_v3[ptr_v3] = 3
    ptr_v3 += 1

    for n in range(5, 1001, 2):   # 대상은 홀수만
        i_v3 = 1
        while prime_v3[i_v3] * prime_v3[i_v3] <= n:  # N 제곱근 이하의 소수의 경우만 한정
            counter_v3 += 2
            if n % prime_v3[i_v3] == 0:
                break  # 소수가 아님
            i_v3 += 1

        else:  # 소수인 경우
            prime_v3[ptr_v3] = n
            ptr_v3 += 1
            counter_v3 += 1

    # 소수 출력
    for i in range(ptr_v3):
        print(prime_v3[i])

    print(f'곱셈과 나눗셈 실행한 횟수 : {counter_v3}')


print_prime_v3()
