"""
    깊은 복사 vs 얕은 복사
"""

import copy

x = [[1, 2, 3], [4, 5, 6]]

y = x.copy()  # 얕은 복사
z = copy.deepcopy(x)  # 깊은 복사

x[0][0] = 999

print(y[0][0])  # 999 -> 원본 객체와 같은 곳 참조
print(z[0][0])  # 1 -> 깊은 복사라 별도 참조
