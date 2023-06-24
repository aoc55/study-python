from typing import Any

"""
    배열을 이용한 고정길이 스택 
"""


class FixedStack:

    # Exception -> Empty
    class Empty(Exception):
        pass

    # Exception -> Full
    class Full(Exception):
        pass

    def __init__(self, capacity: int = 256) -> None:
        # 초기화
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self) -> int:
        return self.ptr

    def is_empty(self) -> bool:
        # '==' 대신 '<=' 사용
        return self.ptr <= 0

    def is_full(self) -> bool:
        # '==' 대신 '>=' 사용
        return self.ptr >= self.capacity

    def push(self, value: Any) -> None:
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        if self.is_empty():
            return FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]

    def clear(self) -> None:
        self.ptr = 0

    def find(self, value: Any) -> Any:
        for i in range(self.ptr - 1, -1, -1):   # 역순으로 찾기
            if self.stk[i] == value:
                return i
        return -1

    def count(self, value: Any) -> int:
        count = 0
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                count += 1
        return count

    def __contains__(self, item: Any) -> bool:
        return self.count(value) > 0

    def dump(self) -> None:
        if self.is_empty():
            print('스택 is Empty')
        else:
            print(self.stk[:self.ptr])


if __name__ == '__main__':
    stack = FixedStack(64)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print("Push complete", end='\n')
    stack.dump()
    print('', end='\n')
    print("Pop Start")
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())  # Exception

