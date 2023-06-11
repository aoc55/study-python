from __future__ import annotations
from typing import Any, Type
import hashlib

'''
    체인 헤시법
'''


# 해시를 구성하는 노드
class Node:
    def __init__(self, key: Any, value: Any, next_node: Node) -> None:
        self.key = key
        self.value = value
        self.next = next_node


# 체인 Hash
class ChainedHash:
    def __init__(self, capacity: int) -> None:
        self.capcity = capacity
        self.table = [None] * self.capcity

    # 해시 값 구하기
    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):  # 정수인경우
            return key % self.capcity
        # 그 외
        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capcity

    # 해시 내 검색
    def search(self, key: Any) -> Any:
        hash_value = self.hash_value(key)  # 1. Hash 값 구하기
        p = self.table[hash_value]  # 2. 버킷 찾아가기

        # 3. 버킷 내 링크드 리스트 순회
        while p is not None:
            if p.key == key:
                return p.value  # 찾았을때
            p = p.next

        return None  # 못 찾았을때

    # 해시 내 값 추가
    def add(self, key: Any, value: Any) -> bool:
        hash_value = self.hash_value(key)
        p = self.table[hash_value]

        while p is not None:
            if p.key == key:
                return False  # 이미 존재하는 Key
            p = p.next  # 마지막까지 순회

        new_node = Node(key, value, self.table[hash_value])  # 맨 앞에 추가
        self.table[hash_value] = new_node
        return True

    # 해시 내 값 삭제
    def remove(self, key: Any) -> bool:
        hash_value = self.hash_value(key)
        p = self.table[hash_value]
        pp = None  # 앞 노드

        while p is not None:
            if p.key == key:  # 찾음
                if pp is None:
                    self.table[hash_value] = p.next
                else:
                    pp.next = p.next  # 앞과 뒤 이어주기
                return True
            pp = p
            p = p.next

        return False  # 없을 경우

    # 해시 내 모든 요소 출력
    def dump(self) -> None:
        for i in range(self.capcity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f' -> {p.key} ({p.value})', end='')
                p = p.next
            print()


if __name__ == '__main__':
    hash_table = ChainedHash(13)
    hash_table.add(10, 10)
    hash_table.add(13, 13)
    hash_table.add(12, 12)
    hash_table.add(20, 20)
    hash_table.add(100, 100)
    hash_table.add(101, 101)
    hash_table.dump()

    print(hash_table.remove(13))
    print(hash_table.remove(8))
    print(hash_table.remove(101))
    hash_table.dump()
