# 해시법

# 데이터의 검색과 더불어 추가 - 삭제도 효율적으로 수행할 수 있다.

# 5 6 14 20 29 34 37 51 69 75 - - -
# 5 6 14 20 29 34 35 37 51 69 75 - -
# 위와 같이 배열에서 '35' 라는 값을 추가

# 1. 이진검색법으로 검사
# 2. 추가 원소가 들어갈 자리의 뒤에 있는 원소를 한칸씩 뒤로 이동
# 3. 추가할 원소를 대입

# 해시값 == 배열의 키 % len(배열)
# 키를 해시값으로 변환 하는 과정을 해시 함수(hash function) 이라고 한다.
# 해시 테이블에서 만들어진 원소를 버킷(bucket)이라고 한다.

# 해시 충돌이란, 해시 테이블에서 만든 버킷이 들어갈 자리에 이미 값이 들어가 있는경우이다.
# 해결 하기 위하여 '체인법', '오픈주소법' 두가지의 방법이 있다.

# 체인법 : 해시값이 같은 원소를 연결 리스트로 관리합니다.
# 오픈 주소법 : 빈 버킷을 찾을 때까지 해시를 반복합니다.

# 체인법으로 해시 함수 구현하기.

from __future__ import annotations
from typing import Any, TypedDict
import hashlib

class Node:
    """해시를 구성하는 노드"""
    def __init__(self, key: Any, value: Any, next: Node) -> None:
        """초기화"""
        self.key = key
        self.value = value
        self.next = next

class ChainedHash:
    """체인법으로 해시 클래스 구현"""

    def __init__(self, capacity: int) -> None:
        """초기화"""
        self.capacity: capacity
        self.table = [None] * self.capacity
    
    def hash_value(self, key: Any) -> int:
        """해시값을 구함"""
        if isinstance(self, key):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(),16) % self.capacity)

    def search(self, key: Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        hash = self.hash_value(key)
        p = self.table[hash]
        
        while p is not None:
            if p.key == key:
                return p.value
            p = p.next

        return None

    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 원소를 추가"""
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return False
            p = p.next

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True
    
    def remove(self, key: Any) -> bool:
        """키가 key인 원소를 삭제"""
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None
        
        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True
            pp = p
            p = p.next
        return False

    def dump(self) -> None:
        """해시 테이블을 덤프"""
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f'  ->{p.key} ({p.value})', end= '')
                p = p.next
            print()

a = ChainedHash(10)
