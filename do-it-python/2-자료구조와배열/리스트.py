# [리스트 비교]
lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 2, 3, 4, 5]
print(lst1 == lst2)  # True
print(lst1 is lst2)  # False

lst3 = [10, 20, 30, 40, 50]
lst4 = lst3  # lst3와 같은 곳을 참조 한다.
print(lst3 == lst4)  # True
print(lst3 is lst4)  # Ture
lst3[0] = 100
print(lst4[0] == 100)  # True


# [리스트 스캔]
x = ['a', 'b', 'c', 'd']
for char in x:
    print(char)

for i in range(len(x)):
    print(x[i])

for i, char in enumerate(x):  # enumerate -> idx 와 value 리턴
    print(i, char)

for i, char in enumerate(x, 10):  # enumerate -> 리턴하는 인덱스의 시작 값 설정 가능
    print(i, char)


