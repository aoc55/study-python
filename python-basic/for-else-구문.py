"""
    for-else 구문 실습
"""

data = [1, 2, 3, 4, 5]

# for ~ else
# (else 구문 수행)
for i in range(len(data)):
    if data[i] > 100:
        break
else:
    print("100보다 큰 수는 없습니다")


# for ~ else
# (else 구문 미수행)
for i in range(len(data)):
    if data[i] > 2:
        break
else:
    print("출력되지 않음")


# while ~ else
# (else 구문 수행)
i = 0
while i < 5:
    i += 1
else:
    print("출력~")


# while ~ else
# (else 구문 미수행)
j = 0
while j < 5:
    j += 1
    if j > 3:
        break
else:
    print("출력되지 않음")
