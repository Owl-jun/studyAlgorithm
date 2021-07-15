# 보초법

# 선형 검색에서 반복할 때마다 2가지 종료 조건을 체크합니다. (검색값을 찾았는지 or 더이상 검색할 자료가 없는지)
# 이 비용을 반으로 줄이는 방법이 보초법 입니다.

import copy
from typing import Any, Sequence

def seq_search(seq: Sequence, key: Any) -> int:
    """시퀀스 seq에서 key와 일치하는 원소를 선형검색(보초법)"""
    a = copy.deepcopy(seq)
    a.append(key)

    i = 0
    while True:
        if a[i] == key:
            break
        i+= 1
    return -1 if i== len(seq) else i

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요. : '))
    x = [None] * num
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    ky = int(input('검색할 값을 입력하세요.: '))
    idx = seq_search(x,ky)

    if idx == -1:
        print('검색결과없음')
    else:
        print(f'x[{idx}]')