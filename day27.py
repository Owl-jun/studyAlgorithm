# 이진 검색

# 이진 검색은 원소가 오름차순이나 내림차순으로 정렬된 배열에서 좀 더 효율적으로 검색할 수 이는 알고리즈입니다.

# 이진검색 알고리즘

from typing import Any, Sequence


def bin_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 일치하는 원소를 이진 검색"""
    pl = 0
    pr = len(a) - 1

    while True:
        pc = (pl + pr) // 2
        if a[pc] == key :
            return pc
        elif a[pc] < key :
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break
    return -1


if __name__ == '__main__' :
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num


    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('검색할 값 입력 : '))
    idx = bin_search(sorted(x),ky)

    if idx == -1:
        print('검색 실패!')
    else:
        print(f'검색 결과는 x[{idx}]에 있습니다.')