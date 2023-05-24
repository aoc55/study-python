# List
my_list = list((1, 2, 3))
my_list_2 = [1, 2, 3]
my_list_3 = range(1, 5)
my_list_4 = [1, "hello", 3.14]
# print(type(my_list_4))


# Tuple
my_tuple = (1, 2, 3)
my_tuple_2 = tuple((1, 2))
my_tuple_3 = (1, "hello", 3.14)
my_single_tuple = (1,)
# print(type(my_single_tuple))


# Unpack
a, b, c = my_list
# print(a, b, c)  # 1, 2, 3


# slicing
slicing_list = list(range(1, 10))
print(slicing_list[1:7:2])  # 1에서 7까지 2개씩 건너 음어라
print(slicing_list[19:20])  # 오류 미발생
print(slicing_list[:10])
print(slicing_list[5:])
print(slicing_list[::2])  # 2개씩 건너 띄기
print(slicing_list[::-1])  # 맨 끝부도 모두 출력


# 식별번호 변경 (Immutable)
n = 5
print(id(n))  # 4366559664
n = "HELLO"
print(id(n))  # 4369464496

x = 10
print(id(x))  # 4311738960
x = x + 1
print(id(x))  # 4311738992 -> 변경됨


# 등가성 <-> 동일성
x = 10
y = 10.0
print(x == y)  # true -> 값이 같은지
print(x is y)  # false -> 참조하는 객체 식별 번호까지 같은지
print(x is x)  # true


# 내포 표기 생성
num = [1, 2, 3, 4, 5, 6]
temp_list = [i * 2 for i in num if i % 2 == 0]
print(temp_list)



