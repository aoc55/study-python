"""
    링크드 리스트 구현해보기
"""

from __future__ import annotations
from typing import Any, Type


# 노드 정의
class Node:
    def __init__(self, data: Any, next: Node = None):
        self.data = data
        self.next = next


# 링크드리스트 정의
class LinkedList:

    def __init__(self):
        self.no = 0
        self.head = None
        self.current = None

    def __len__(self):
        return self.no

    def __contains__(self, item):
        return True if self.search(item) != -1 else False

    def search(self, data:Any) -> int:  # 검색 결과로 위치를 반환
        cnt = 0
        ptr = self.head     # 시작점

        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next

        return -1       # 탈출조건

    def add_first(self, data: Any) -> None:
        ptr = self.head
        self.head = Node(data, ptr)
        self.current = self.head
        self.no += 1

    def add_last(self, data: Any) -> None:
        if self.head is None:
            self.add_first(data)
        else:
            ptr = self.head

            while ptr.next is not None:
                ptr = ptr.next

            ptr.next = Node(data, None)
            self.current = ptr.next
            self.no += 1

    def remove_first(self) -> None:
        if self.head is not None:
            self.head = self.head.next
            self.current = self.head
            self.no -= 1

    def remove_last(self):
        if self.head is not None:

            if self.head.next is None :
                self.remove_first()

            else:
                pre = self.head
                ptr = pre.next

                while ptr is not None:
                    pre = ptr
                    ptr = ptr.next

                pre.next = None
                self.current = pre
                self.no -= 1

    def remove(self, p: Node) -> None:

        if self.head is not None:
            if p is self.head:
                self.remove_first()
            else:
                ptr = self.head

                while ptr.next is not p:
                    ptr = ptr.next
                    if ptr is None:
                        return

                ptr.next = p.next
                self.current = ptr
                self.no -= 1

    def print(self) -> None:
        ptr = self.head
        while ptr is not None:
            if ptr.next is not None:
                print(f'[{ptr.data}] -> ', end='')
            else:
                print(f'[{ptr.data}]', end='')
            ptr = ptr.next

    # Iteration
    def __iter__(self):
        return LinkedListIterator(self.head)


class LinkedListIterator:

    def __init__(self, head: Node):
        self.current = head

    def __iter__(self) -> LinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data


if __name__ == '__main__':
    lst = LinkedList()

    for i in range(1, 11, 1):
        lst.add_last(i)
    lst.print()

    print("")

    lst.remove_first()
    lst.remove_first()
    lst.remove_first()
    lst.print()

    print("")

    lst.add_last(20)
    lst.add_last(21)
    lst.add_last(22)
    lst.print()

    print("")

    print(f'search -> {lst.search(20)}')
