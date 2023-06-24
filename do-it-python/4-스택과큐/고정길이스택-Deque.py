from typing import Any
from collections import deque

"""
    Collections.Dequeue 을 이용한 고정길이 스택 
"""


class Stack:

    def __init__(self, maxlen: int = 256) -> None:
        # 초기화
        self.capacity = maxlen
        self.__stk = deque([], maxlen)

    def __len__(self) -> int:
        return len(self.__stk)

    def is_empty(self) -> bool:
        return not self.__stk

    def is_full(self) -> bool:
        return len(self.__stk) == self.__stk.maxlen

    def push(self, value: Any) -> None:
        self.__stk.append(value)

    def pop(self) -> Any:
        return self.__stk.pop()

    def peek(self) -> Any:
        return self.__stk[-1]

    def clear(self) -> None:
        self.__stk.clear()

    def find(self, value: Any) -> Any:
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1

    def count(self, value: Any) -> int:
        return self.__stk.count(value)

    def __contains__(self, value: Any) -> bool:
        return self.count(value)

    def dump(self) -> None:
        print(list(self.__stk))


if __name__ == '__main__':
    stack = Stack(64)
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
