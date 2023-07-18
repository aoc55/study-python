from typing import Any

"""
    링버퍼 기반의 큐
"""


class FixedQueue:

    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int) -> None:
        self.no = 0     # 데이터 갯수
        self.front = 0  # 맨 앞 원소 커서
        self.rear = 0   # 맨 뒤 원소 커서
        self.capacity = capacity    # 큐의 크기
        self.que = [None] * capacity    # 큐 본체

    def __len__(self):
        return self.no

    def is_empty(self):
        return self.no <= 0

    def is_full(self):
        return self.no >= self.capacity

    def enque(self, x: Any) -> None:
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self) -> Any:
        if self.is_empty():
            return FixedQueue.Empty
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]

    def find(self, value: Any) -> Any:       # 선형검색 기반
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                return idx
        return -1

    def count(self, value: Any) -> int:
        c = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                c += 1
        return c

    def __contains__(self, item) -> bool:
        return self.find(item) >= 0

    def clear(self):
        # 배열 자체를 비울 필요는 없음
        self.no = 0
        self.front = 0
        self.rear = 0

    def dump(self) -> None:
        if self.is_empty():
            print('Queue is Empty')
        else:
            for i in range(self.no):
                idx = (i + self.front) % self.capacity
                print(f'{idx} -> {self.que[idx]}')
        print()


if __name__ == '__main__':
    queue = FixedQueue(10)
    queue.enque('a')
    queue.enque('b')
    queue.enque('c')
    queue.enque('d')
    queue.enque('e')
    queue.dump()
    print()
    queue.deque()
    queue.deque()
    queue.dump()
    print()
    queue.enque('가')
    queue.enque('나')
    queue.enque('다')
    queue.enque('라')
    queue.enque('마')
    queue.enque('바')
    queue.enque('사')
    queue.dump()
    print()




