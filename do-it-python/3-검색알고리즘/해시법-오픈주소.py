"""
    Hash 구현
    - 충돌 시 오픈주소법을 통한 재해싱 수행
"""

from typing import Any, Type
from enum import Enum
import hashlib


class Status(Enum): # 버킷 속성 정의
    OCCUPIED = 0    # 데이터 보유
    EMPTY = 1       # 비어 있음
    DELETED = 2     # 삭제 완료


class Bucket:   # 해시 테이블 내 버킷 정의
    # 생성자
    def __init__(self, key: Any = None, value: Any = None, stat: Status = Status.EMPTY) -> None:
        self.key = key
        self.value = value
        self.stat = stat

    # set
    def set(self, key: Any, value: Any, stat: Status) -> None:
        self.key = key
        self.value = value
        self.stat = stat

    # set stat
    def set_stat(self, stat: Status):
        self.stat = stat


class OpenHash:     # OpenHashTable 정의
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity                      # 해시테이블 크기 지정
        self.table = [Bucket()] * self.capacity     # 해시테이블

    def hash_value(self, key: Any):     # 해시값 구하기
        if isinstance(key, int):
            return key % self.capacity
        return int(hashlib.md5(str(key).encode()).hexdigest(), 16) % self.capacity

    def rehash_value(self, key: Any):       # 재해시
        return (self.hash_value(key) + 1) % self.capacity

    def search_node(self, key: Any) -> Any:
        hash_value = self.hash_value(key)
        p = self.table[hash_value]

        for i in range(self.capacity):
            if p.stat == Status.EMPTY:                          # Empty
                break
            elif p.stat == Status.OCCUPIED and p.key == key:    # Found
                return p
            hash_value = self.rehash_value(key)     # ReHash
            p = self.table[hash_value]

        return None

    def search(self, key: Any) -> Any:
        p = self.search_node(key)
        if p is not None:
            return p.value
        else:
            return None

    def add(self, key: Any, value: Any) -> bool:

        # 이미 등록되었는지 확인
        if self.search(key) is not None:
            return False

        hash_value = self.hash_value(key)
        p = self.table[hash_value]

        for i in range(self.capacity):
            # 추가
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash_value] = Bucket(key, value, Status.OCCUPIED)
                return True
            # 재해시
            hash_value = self.rehash_value(key)
            p = self.table[hash_value]

        return False

    def remove(self, key: Any) -> int:
        p = self.search_node(key)

        if p is None:
            return False

        p.set_stat(Status.DELETED)
        return True

    def dump(self) -> None:
        for i in range(self.capacity):
            print(f'{i:}', end=' ')
            bucket = self.table[i]
            if bucket.stat == Status.OCCUPIED:
                print(f'{bucket.key} ({bucket.value})')
            elif bucket.stat == Status.EMPTY:
                print('-- 미등록 --')
            elif bucket.stat == Status.DELETED:
                print('-- 삭제완료 --')


# Test
if __name__ == '__main__':
    hash_table = OpenHash(13)

    # 데이터 추가
    hash_table.add(1, '수연')
    hash_table.add(5, '동혁')
    hash_table.add(10, '예지')
    hash_table.add(12, '원준')
    hash_table.add(14, '민서')

    # 덤프
    hash_table.dump()
    print(end="\n")

    # 검색
    result = hash_table.search(5)
    print(f'검색결과 = {result}', en)

    # 삭제
    hash_table.remove(10)
    print(f'Key: 10 삭제완료', end='\n\n')

    # 덤프
    hash_table.dump()
    print(end="\n")


